"""
Sample module depending on another module.
In this case, this module depends on `wordcount.py`.
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import pyspark
import os

import projectname.wordcount as wordcount
import projectname.util as util


def word_counts(sc, filename):
    """word_counts

    :param sc:
    :type sc: pyspark.SparkContext
    :param filename:

    :return: word and counts.
    :rtype: dict
    """

    lines = sc.textFile(filename, minPartitions=5)
    results = wordcount.do_word_counts(lines)
    return results


def group_by_age(spark, filename):
    """word_counts

    :param spark:
    :type spark: pyspark.sql.SparkSession
    :param filename:

    :return: word and counts.
    :rtype: dict
    """

    df = spark.read.option('header', 'true').csv(filename)
    results = wordcount.do_group_by_age(df)
    return results


def string_to_row(spark, filename):
    df = spark.read.option('header', 'true').csv(filename)
    results = wordcount.do_string_to_row(df)
    return results


def main():
    config = [
        ('spark.master', 'yarn'),
    ]
    spark_conf = util.create_spark_conf(config)
    sc = util.get_or_create_spark_context(spark_conf)
    spark = util.get_or_create_spark_session(sc)

    path_to_this_dir = os.path.abspath(os.path.dirname(__file__))
    path_to_data_dir = os.path.join(path_to_this_dir, '../data')
    path_to_txt = os.path.join(path_to_data_dir, 'data.txt')
    path_to_csv = os.path.join(path_to_data_dir, 'data.csv')
    path_to_data1_txt = os.path.join(path_to_data_dir, 'data1.txt')
    print(word_counts(sc, path_to_txt))
    print(group_by_age(spark, path_to_csv))
    print(string_to_row(spark, path_to_data1_txt))


if __name__ == '__main__':
    main()
