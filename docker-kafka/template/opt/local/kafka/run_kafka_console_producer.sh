#!/bin/bash

kafka-console-producer.sh \
  --broker-list kafka-server:9094 \
  --topic test-topic \
  --producer.config config_custom/client_security.properties
