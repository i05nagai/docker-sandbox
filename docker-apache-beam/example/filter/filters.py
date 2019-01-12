"""An example workflow that demonstrates filters and other features.
  - Reading and writing data from BigQuery.
  - Manipulating BigQuery rows (as Python dicts) in memory.
  - Global aggregates.
  - Filtering PCollections using both user-specified parameters
    as well as global aggregates computed during pipeline execution.
"""

from __future__ import absolute_import

import argparse
import logging

import apache_beam as beam
from apache_beam.pvalue import AsSingleton
import os
PATH_TO_THIS_DIR = os.path.abspath(os.path.dirname(__file__))


def filter_cold_days(p, input_data, month_filter):
    """Workflow computing rows in a specific month with low temperatures.
    Args:
      input_data: a PCollection of dictionaries representing table rows. Each
        dictionary must have the keys ['year', 'month', 'day', and 'mean_temp'].
      month_filter: an int representing the month for which colder-than-average
        days should be returned.
    Returns:
      A PCollection of dictionaries with the same keys described above. Each
        row represents a day in the specified month where temperatures were
        colder than the global mean temperature in the entire dataset.
    """

    # Project to only the desired fields from a complete input row.
    # E.g., SELECT f1, f2, f3, ... FROM InputTable.
    projection_fields = ['month', 'mean_temp']
    fields_of_interest = (
        input_data
        | 'Projected' >> beam.Map(
            lambda row: {f: row[f] for f in projection_fields}))

    # Compute the global mean temperature.
    global_mean = AsSingleton(
        fields_of_interest
        | 'ExtractMean' >> beam.Map(lambda row: row['mean_temp'])
        | 'GlobalMean' >> beam.combiners.Mean.Globally())
    global_mean = AsSingleton(
        p
        | beam.Create([
            1000
        ])
    )

    # Filter to the rows representing days in the month of interest
    # in which the mean daily temperature is below the global mean.
    return (
        fields_of_interest
        | 'DesiredMonth' >> beam.Filter(lambda row: row['month'] == month_filter)
        | 'BelowMean' >> beam.Filter(
            lambda row, mean: row['mean_temp'] < mean, global_mean))


def run(argv=None):
    """Constructs and runs the example filtering pipeline."""

    parser = argparse.ArgumentParser()
    parser.add_argument('--month_filter',
                        default=7,
                        help='Numeric value of month to filter on.')
    known_args, pipeline_args = parser.parse_known_args(argv)

    with beam.Pipeline(argv=pipeline_args) as p:
        input_data = (
            p
            | 'create' >> beam.Create([
                {'month': 1, 'mean_temp': 1},
                {'month': 2, 'mean_temp': 2},
                {'month': 3, 'mean_temp': 3},
                {'month': 7, 'mean_temp': 1},
                {'month': 7, 'mean_temp': 5},
                {'month': 7, 'mean_temp': 2},
            ])
        )

        # pylint: disable=expression-not-assigned
        path_output = os.path.join(PATH_TO_THIS_DIR, 'foobar.txt')
        (filter_cold_days(p, input_data, known_args.month_filter)
         | beam.io.WriteToText(path_output, file_name_suffix='.csv'))


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    run()
