#!/bin/bash

${KAFKA_HOME}/bin/kafka-topics.sh \
  --describe \
  --zookeeper kafka-zookeeper:2181 \
  --topic test
