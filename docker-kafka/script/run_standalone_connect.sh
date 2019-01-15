#!/bin/bash

${KAFKA_HOME}/bin/connect-standalone.sh \
  config/connect-standalone.properties \
  config/connect-file-source.properties \
  config/connect-file-sink.propertie
