from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
import operator
import pyspark


def get_logger(sc, name):
    """get_logger

    :param name:

    Example
    ========

    >>> logger = get_logger(sc, __name__)
    >>> logger.info("pyspark script logger initialized")
    """

    log4j = sc._jvm.org.apache.log4j
    return log4j.LogManager.getLogger(name)


if __name__ == "__main__":
    conf = pyspark.SparkConf(
    ).setMaster(
        'local[*]'
    ).setAppName(
        'pyspark-local'
    )
    sc = pyspark.SparkContext(conf=conf)
    spark = pyspark.sql.SparkSession(sc)
    logger = get_logger(sc, __name__)

    path_to_csv = 'data/data.csv'
    df = spark.read.option("header", "true").csv(path_to_csv)
    lines = df.rdd

    # counts by age
    counts = (lines
              .map(lambda x: (x[3], 1))
              .reduceByKey(operator.add)
              )
    results = {word: count for word, count in counts.collect()}
    logger.info(results)
    print(results)
