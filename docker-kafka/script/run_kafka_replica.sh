#!/bin/bash

${KAFKA_HOME}/bin/kafka-server-start.sh config/server-1.properties &
${KAFKA_HOME}/bin/kafka-server-start.sh config/server-2.properties &
