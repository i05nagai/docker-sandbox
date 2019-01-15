#!/bin/bash

${KAFKA_HOME}/bin/kafka-topics.sh \
  --describe \
  --zookeeper localhost:2181 \
  --topic test
