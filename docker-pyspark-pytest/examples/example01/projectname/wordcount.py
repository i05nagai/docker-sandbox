from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StringType, StructField

import operator
from . import util


def do_word_counts(lines):
    """
    count of words in an rdd of lines

    :param lines: lines of text
    :type lines: pyspark.RDD

    :return:
    :rtype: dict
    """
    counts = (lines
              .flatMap(lambda x: x.split())
              .map(lambda x: (x, 1))
              .reduceByKey(operator.add)
              )
    results = {word: count for word, count in counts.collect()}
    util.get_logger(
        lines.context, __name__).info('Results: {0}'.format(results))
    return results


def do_group_by_age(lines):
    """
    count of words in an rdd of lines

    :param lines:
    :type lines: pyspark.sql.DataFrame

    :return:
    :rtype: dict
    """
    lines_rdd = lines.rdd
    counts = (lines_rdd
              .map(lambda row: (row['age'], 1))
              .reduceByKey(operator.add)
              )
    results = {word: count for word, count in counts.collect()}
    return results


def do_string_to_row(df):
    schema = StructType().add(
        "parent1", StructType().add(
            "value11", StringType()
        ).add(
            "value12", StringType())
    ).add(
        "parent2", StructType().add(
            "value21", StringType()
        ).add(
            "value22", StringType()
        )
    )
    df = df.select(F.from_json(F.decode("value", "UTF-8"), schema).alias("value"))
    results = [row.asDict(True) for row in df.collect()]
    return results
