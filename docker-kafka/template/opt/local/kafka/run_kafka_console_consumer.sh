#!/bin/bash

${KAFKA_HOME}/bin/kafka-console-consumer.sh \
  --bootstrap-server kafka-server:9093 \
  --topic test-topic \
  --consumer.config config_custom/client_security.properties
