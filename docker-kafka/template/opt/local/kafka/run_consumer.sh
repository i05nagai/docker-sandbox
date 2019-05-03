#!/bin/bash

${KAFKA_HOME}/bin/kafka-console-consumer.sh --bootstrap-server kafka-server:9092 --topic test --from-beginning
