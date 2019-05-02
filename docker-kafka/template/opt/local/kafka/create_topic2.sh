#!/bin/bash

${KAFKA_HOME}/bin/kafka-topics.sh \
  --create --zookeeper localhost:2181 \
  --replication-factor 3 \
  --partitions 1 \
  --topic my-replicated-topic
