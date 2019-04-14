import logging
import pyspark
import pytest


def quiet_py4j():
    """ turn down spark logging for the test context """
    logger = logging.getLogger('py4j')
    logger.setLevel(logging.WARN)


@pytest.fixture(scope="session")
def spark_context(request):
    """spark_context
    fixture for creating a SparkContext.

    :param request: pytest.FixtureRequest object.
    :return: SparkContext for test.
    :rtype: SparkContext

    Example
    ========
    >>> @pytest.mark.usefixtures("spark_context")
    >>> def do_something_test(spark_context):
    >>>     # input
    >>>     test_input = [
    >>>         ' hello spark ',
    >>>         ' hello again spark spark'
    >>>     ]
    >>>     # create input rdd
    >>>     input_rdd = spark_context.parallelize(test_input, 1)
    >>>     # execute function
    >>>     actual = test_target.do_something(input_rdd)
    >>>     # check result
    >>>     expect = {'hello':2, 'spark':3, 'again':1}
    >>>     assert expect == actual
    """
    conf = pyspark.SparkConf(
    ).setMaster(
        "local"
    ).setAppName(
        "pytest-pyspark-local-testing"
    )
    sc = pyspark.SparkContext.getOrCreate(conf=conf)
    request.addfinalizer(lambda: sc.stop())

    quiet_py4j()
    return sc


@pytest.fixture(scope="session")
def spark_session(request):
    """spark_session
    fixture for creating a SparkSession.
    :param request: pytest.FixtureRequest object.
    :return: SparkSession for test.
    :rtype: SparkSession
    Example
    ========
    >>> @pytest.mark.usefixtures("spark_session")
    >>> def do_something_test(spark_session):
    >>>     # input
    >>>     test_input = [
    >>>         ' hello spark ',
    >>>         ' hello again spark spark'
    >>>     ]
    >>>     # create input rdd
    >>>     input_dataframe = spark_session.createDataFrame(test_input)
    >>>     # execute function
    >>>     actual = test_target.do_something(input_dataframe)
    >>>     # check result
    >>>     expect = {'hello':2, 'spark':3, 'again':1}
    >>>     assert expect == actual
    """
    spark = (pyspark.sql.SparkSession
             .builder
             .master('local[*]')
             .appName('pytest-pyspark-sql-local-testing')
             .config('spark.debug.maxToStringFields', 1000)
             .getOrCreate())
    request.addfinalizer(lambda: spark.stop())

    quiet_py4j()
    return spark
