"""
Sample module depending on another module.
In this case, this module depends on `wordcount.py`.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import pyspark
import os

from . import wordcount


def word_counts(sc, filename):
    """word_counts

    :param filename:

    :return: word and counts.
    :rtype: dict
    """

    lines = sc.textFile(filename, 1)
    results = wordcount.do_word_counts(lines)
    return results


def group_by_age(spark, filename):
    """word_counts

    :param filename:

    :return: word and counts.
    :rtype: dict
    """

    df = spark.read.option('header', 'true').csv(path_to_csv)
    results = wordcount.do_gorup_by_age(df)
    return results


if __name__ == "__main__":
    conf = pyspark.SparkConf(
    ).setMaster(
        'local[*]'
    ).setAppName(
        'pyspark-sample'
    )
    sc = pyspark.SparkContext(conf=conf)
    spark = pyspark.sql.SparkSession(sc)

    path_to_this_dir = os.path.abspath(os.path.dirname(__file__))
    path_to_data_dir = os.path.join(path_to_this_dir, '../data')
    path_to_txt = os.path.join(path_to_data_dir, 'data.txt')
    path_to_csv = os.path.join(path_to_data_dir, 'data.csv')
    print(word_counts(sc, path_to_txt))
    print(group_by_age(spark, path_to_csv))
