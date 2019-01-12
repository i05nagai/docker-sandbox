import apache_beam as beam
import apache_beam.options.pipeline_options as pipeline_options
import os
import logging
PATH_TO_THIS_DIR = os.path.abspath(os.path.dirname(__file__))


def main():
    with beam.Pipeline(options=pipeline_options.PipelineOptions()) as p:
        #
        # create
        #
        p_create = (
            p
            | 'create' >> beam.Create([
                {'a': 1},
                {'a': 2},
                {'a': 3},
            ])
        )
        p_single = (
            p
            | beam.Create([
                1
            ])
        )
        p_filter = beam.pvalue.AsSingleton(
            p_create
            | beam.Filter(lambda row: row['a'] == 2)
        )
        p_process = (
            p_create
            | beam.Map(lambda row, val: {'a': row['a'], 'b': val['a']}, p_filter)
        )
        path_output = os.path.join(PATH_TO_THIS_DIR, 'foobar.txt')
        (p_process
         | beam.io.WriteToText(path_output, file_name_suffix='.csv'))


if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    main()
