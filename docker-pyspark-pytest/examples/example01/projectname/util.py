import pyspark


def create_spark_conf(config=[]):
    default_config = [
        ('spark.app.name', 'pyspark-sample'),
        ('spark.master', 'local[*]'),
    ]
    conf = pyspark.SparkConf().setAll(pairs=default_config + config)
    return conf


def get_or_create_spark_context(conf):
    """get_or_create_spark_context

    :param conf:
    :type conf: pyspark.SparkConf
    """
    sc = pyspark.SparkContext.getOrCreate(conf=conf)
    return sc


def get_or_create_spark_session(sc):
    """get_or_create_spark_context

    :param sc:
    :type conf: pyspark.SparkContext
    """
    spark_session = pyspark.sql.SparkSession(sc).builder.getOrCreate()
    return spark_session


def get_logger(sc, name):
    log4jLogger = sc._jvm.org.apache.log4j
    logger = log4jLogger.LogManager.getLogger(name)
    return logger
