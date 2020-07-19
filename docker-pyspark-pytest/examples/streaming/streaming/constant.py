import os


STREAM_READER_KAFKA_DEFAULT_OPTIONS = {
    "kafka.bootstrap.servers": os.environ.get('KAFKA_BOOTSTRAP_SERVERS'),
    "kafka.security.protocol": "SASL_SSL",
    "kafka.sasl.mechanism": "PLAIN",
    "kafka.ssl.truststore.location": os.environ.get('KAFKA_SSL_TRUSTSTORE_LOCATION'),
    "kafka.ssl.truststore.password": os.environ.get('KAFKA_SSL_TRUSTSTORE_PASSWORD'),
    "startingOffsets": os.environ.get('STARTING_OFFSETS'),
    "maxOffsetsPerTrigger": os.environ.get('MAX_OFFSETS_PER_TRIGGER'),
    "failOnDataLoss": 'false',
}

STREAM_WRITER_DEFAULT_OPTIONS = {
    'checkpointLocation': os.environ.get('CHECKPOINT_LOCATION'),
}

SPARK_CONF_DEFAULT = [
    ('spark.app.name', ''),
    # https://spark.apache.org/docs/latest/submitting-applications.html#master-urls
    ('spark.master', 'local[*]'),
]
