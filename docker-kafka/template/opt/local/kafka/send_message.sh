#!/bin/bash

${KAFKA_HOME}/bin/kafka-console-producer.sh --broker-list kafka-server:9092 --topic test
