import pyspark


def create_spark_context():
    conf = pyspark.SparkConf(
    ).setMaster(
        'local[*]'
    ).setAppName(
        'pyspark-sample'
    )
    sc = pyspark.SparkContext(conf=conf)
    return sc


def get_logger(name):
    sc = create_spark_context()
    log4jLogger = sc._jvm.org.apache.log4j
    logger = log4jLogger.LogManager.getLogger(name)
    return logger
