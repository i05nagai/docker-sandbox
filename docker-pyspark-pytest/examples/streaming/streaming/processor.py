from . import transform
from . import util
import pyspark.sql.functions as functions


def rename_column(df, schema):
    df_processed = (
        df
        # .select(
        #     functions.from_json('json_col', schema).alias('json_col')
        # ).select(
        #     functions.col('json_col.col1').alias('col1')
        # )
    )
    return df_processed


# https://spark.apache.org/docs/latest/api/python/pyspark.sql.html#module-pyspark.sql.functions
def process_socket(config, schema, options={}):
    spark_session = util.get_spark_session(config)
    logger = util.get_logger(spark_session, __name__)

    options = dict()
    df = transform.read_stream_from_socket(spark_session, options)

    df_processed = rename_column(df, schema)

    def writer(row):
        row.asDict()
        row['aaaa']

    try:
        transform.write_stream_to_console(df_processed, options, writer)
    except Exception as e:
        print(e)
        # logger.info(e)


# https://spark.apache.org/docs/latest/api/python/pyspark.sql.html#module-pyspark.sql.functions
def process_file(config, schema, options={}):
    spark_session = util.get_spark_session(config)
    logger = util.get_logger(spark_session, __name__)

    options = dict()
    df = transform.read_stream_from_file(spark_session, options)

    df_processed = rename_column(df, schema)

    def writer(row):
        row.asDict()
        row['aaaa']

    try:
        transform.write_stream_to_console(df_processed, options, writer)
    except Exception as e:
        print(e)
        # logger.info(e)
