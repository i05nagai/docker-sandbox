#!/bin/bash

${KAFKA_HOME}/bin/kafka-console-consumer.sh \
  --bootstrap-server localhost:9092 \
  --from-beginning \
  --topic my-replicated-topic
