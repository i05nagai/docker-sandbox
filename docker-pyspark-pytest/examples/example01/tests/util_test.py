import pytest
import projectname.util as util


def test_create_spark_conf():
    conf = util.create_spark_conf()
    sc = util.get_or_create_spark_context(conf)
    spark = util.get_or_create_spark_session(sc)
    print(spark)
    print(spark.sparkContext.getConf().getAll())
    assert False
