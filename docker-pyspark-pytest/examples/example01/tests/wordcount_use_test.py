import pytest
import projectname.wordcount_use as target
import builtins


@pytest.mark.usefixtures("spark_context")
def test_word_counts(spark_context, mocker):
    """ test word couting
    Args:
        spark_context: test fixture SparkContext
    """
    # noqa
    # this is for package dependecies issues. See
    # https://www.cloudera.com/documentation/enterprise/5-5-x/topics/spark_python.html
    # spark_context.addPyFile(target.__file__)

    filename = ''
    input_data = [
        ' hello spark ',
        ' hello again spark spark'
    ]
    input_rdd = spark_context.parallelize(input_data, 1)

    spark_context = mocker.Mock()
    spark_context.textFile.return_value = input_rdd

    # if you want to mock methods in wordcount
    # mocker.patch.object(target.wordcount, 'do_word_counts')
    # target.wordcount.do_word_counts.return_value = {1: 1}

    actual = target.word_counts(spark_context, filename)

    expect = {
        'hello': 2,
        'spark': 3,
        'again': 1
    }
    assert expect == actual
