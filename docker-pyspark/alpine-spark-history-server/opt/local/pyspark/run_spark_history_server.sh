#!/bin/bash

${SPARK_VERSION}/sbin/start-master.sh
${SPARK_HOME}/sbin/start-history-server.sh
# not to stop container
tail -f /dev/null
