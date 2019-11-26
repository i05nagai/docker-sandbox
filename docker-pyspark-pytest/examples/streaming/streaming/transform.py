from . import constant


def read_stream_from_socket(spark_session, options):
    options = {
        'host': 'localhost',
        'port': '9999',
    }
    return (spark_session
            .readStream
            .format('socket')
            .options(**options).load())


# https://spark.apache.org/docs/latest/structured-streaming-programming-guide.html
def read_stream_from_file(spark_session, options):
    options = {
        'path': 'file:///tmp/data01.json',
    }
    format = "csv"
    return (spark_session
            .readStream
            .format(format)
            .options(**options).load())


def read_stream_from_kafka(
        spark_session, options):
    stream_reader = spark_session.readStream.format('kafka')
    stream_reader.options(**constant.KAFKA_DEFAULT_OPTIONS)
    stream_reader.options(**options)
    return stream_reader.load()


def read_stream_from_kafka_topic(spark_session, options, topic_name):
    options = {
        'subscribe': topic_name
    }
    return read_stream_from_kafka(spark_session, options)


def write_stream(spark_session, options, writer, output_mode):
    stream_writer = spark_session.writeStream

    stream_writer.options(**constant.STREAM_WRITER_DEFAULT_OPTIONS)
    stream_writer.options(**options)

    stream_writer.foreach(writer)

    output = (stream_writer
              .outputMode(output_mode)
              .trigger(processingTime="2 seconds")
              .start())

    output.awaitTermination()


def write_stream_to_console(spark_session, options, writer, output_mode='update'):
    format = 'json'
    stream_writer = spark_session.writeStream.format(format)
    options = {
        'truncate': False,
        'path': 'file:///tmp/output.json'
    }

    stream_writer.options(**constant.STREAM_WRITER_DEFAULT_OPTIONS)
    stream_writer.options(**options)

    stream_writer.foreach(writer)

    output = (stream_writer
              .outputMode(output_mode)
              .trigger(processingTime="2 seconds")
              .start())

    output.awaitTermination()
