#!/bin/bash

# export KAFKA_OPTS=-Djava.security.auth.login.config=/etc/kafka/kafka_server_jaas.conf
export KAFKA_OPTS=-Djava.security.auth.login.config=/tmp/repository/opt/local/kafka/config_custom/kafka_server_jaas.conf
${KAFKA_HOME}/bin/kafka-server-start.sh config_custom/server.properties
