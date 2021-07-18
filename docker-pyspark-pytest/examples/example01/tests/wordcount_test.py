import pytest
import projectname.wordcount as wordcount
import pyspark.sql.types as types
import json


@pytest.mark.usefixtures("spark_context")
def test_do_word_counts(spark_context):
    """ test word couting
    sample tests using rdd

    :param spark_context: test fixture SparkContext
    """
    test_input = [
        ' hello spark ',
        ' hello again spark spark'
    ]
    input_rdd = spark_context.parallelize(test_input, 1)

    actual = wordcount.do_word_counts(input_rdd)

    expect = {
        'hello': 2,
        'spark': 3,
        'again': 1
    }
    assert expect == actual


@pytest.mark.usefixtures("spark_session")
def test_do_gorup_by_age(spark_session, faker):
    """ test word couting
    sample tests using df

    :param spark_session: test fixture SparkSession
    """
    def to_datetime(dt):
        import datetime
        # from faker date_time to datetime.datetime
        return datetime.datetime(
            dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)

    schema = types.StructType([
        types.StructField('event_timestamp', types.TimestampType(), True),
        types.StructField('user_id', types.StringType(), True),
        types.StructField('referrer', types.StringType(), True),
        types.StructField('age', types.IntegerType(), True),
    ])
    # column data
    event_timestamp = to_datetime(faker.date_time())
    user_id = faker.pystr()
    referrer = faker.pystr()
    age = faker.pyint()
    input_list = [
        (event_timestamp, user_id, referrer, age),
    ]
    df = spark_session.createDataFrame(input_list, schema)

    actual = wordcount.do_group_by_age(df)
    expect = {
        age: 1,
    }
    assert expect == actual


@pytest.mark.usefixtures("spark_session")
def test_string_to_row(spark_session, faker):
    """ test word couting
    sample tests using df

    :param spark_session: test fixture SparkSession
    """
    user_id = faker.pystr()
    referrer = faker.pystr()
    age = faker.pyint()
    input_list = [
        json.dumps({
            "parent1": {
                "value11": "11",
                "value12": 12,
            },
            "parent2": {
                "value21": 21,
            }
        }),
        "a,b,c",
    ]
    df = spark_session.createDataFrame(input_list, types.StringType())

    actual = wordcount.do_string_to_row(df)
    expect = [
        {
            "value": {
                "parent1": {
                    "value11": "11",
                    "value12": "12",
                },
                "parent2": {
                    "value21": "21",
                    "value22": None,
                }
            }
        },
        {
            "value": None
        },
              ]
    assert expect == actual
