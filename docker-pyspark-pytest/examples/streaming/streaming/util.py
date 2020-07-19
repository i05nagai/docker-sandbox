from pyspark.sql.types import ArrayType
from pyspark.sql.types import BinaryType
from pyspark.sql.types import BooleanType
from pyspark.sql.types import ByteType
from pyspark.sql.types import DataType
from pyspark.sql.types import DateType
from pyspark.sql.types import DecimalType
from pyspark.sql.types import DoubleType
from pyspark.sql.types import FloatType
from pyspark.sql.types import IntegerType
from pyspark.sql.types import LongType
from pyspark.sql.types import MapType
from pyspark.sql.types import NullType
from pyspark.sql.types import ShortType
from pyspark.sql.types import StringType
from pyspark.sql.types import StructField
from pyspark.sql.types import StructType
from pyspark.sql.types import TimestampType
import pyspark
from . import constant


SPARK_CONF = (
    pyspark
    .SparkConf()
    .setAll(constant.SPARK_CONF_DEFAULT))


MAP_STRING_TO_TYPE = {
    'DataType': DataType,
    'NullType': NullType,
    'StringType': StringType,
    'BinaryType': BinaryType,
    'BooleanType': BooleanType,
    'DateType': DateType,
    'TimestampType': TimestampType,
    'DecimalType': DecimalType,
    'DoubleType': DoubleType,
    'FloatType': FloatType,
    'ByteType': ByteType,
    'IntegerType': IntegerType,
    'LongType': LongType,
    'ShortType': ShortType,
    'ArrayType': ArrayType,
    'MapType': MapType,
    'StructField': StructField,
    'StructType': StructType,
}


def _json_to_schema(json_dict, schema):
    print(json_dict)
    print(schema)
    if isinstance(json_dict, list):
        sub_schema = _json_to_schema(json_dict[0], None)
        return _json_to_schema(json_dict[0], ArrayType(sub_schema))
    elif isinstance(json_dict, dict):
        for k, v in json_dict.items():
            print(k, v)
            if isinstance(v, dict):
                sub_schema = _json_to_schema(json_dict[k], StructType())
                schema.add(k, sub_schema)
            elif isinstance(v, list):
                sub_schema = _json_to_schema(json_dict[k][0], None)
                schema.add(k, ArrayType(sub_schema))
            else:
                schema.add(k, MAP_STRING_TO_TYPE[v]())
        return schema
    else:
        return MAP_STRING_TO_TYPE[json_dict]()


def json_to_schema(json_str):
    """json_to_schema

    :param json_str:

    json_str = {
        'col1': 'IntegerType',
        'col2': 'FloatType',
        'col3': 'StringType',
        'col4': ['StringType'],
        'col5': [['StringType']],
        'col6': [{
            'col61': 'StringType',
        }],
        'col5': {
            'col1': 'StringType',
            'col2': 1,
            'col3': ['type1'],
        }
    }
    """

    return _json_to_schema(json_str, StructType())


# https://spark.apache.org/docs/2.4.0/api/python/pyspark.html#pyspark.SparkContext
def get_spark_conf(config):
    """get_spark_conf

    :param app_name:
    http://spark.apache.org/docs/2.4.0/api/python/pyspark.html?highlight=sparkconf#pyspark.SparkConf
    config = [
        ('spark.driver.memory', '1g')
        ('spark.executor.memory', '1g')
    ]
    """
    return SPARK_CONF.setAll(config)


def get_spark_session(config):
    spark_conf = get_spark_conf(config)
    spark_session = pyspark.sql.SparkSession.builder.config(conf=spark_conf).getOrCreate()
    spark_session.sparkContext.setLogLevel('DEBUG')
    return spark_session


def get_spark_context(config):
    spark_conf = get_spark_conf(config)
    return pyspark.SparkContext.getOrCreate(spark_conf)


def get_spark_context_from_spark_session(spark_session):
    return spark_session.sparkContext


def get_logger(spark_session, name):
    spark_context = get_spark_context_from_spark_session(spark_session)
    log4jLogger = spark_context._jvm.org.apache.log4j
    logger = log4jLogger.LogManager.getLogger(name)
    return logger
