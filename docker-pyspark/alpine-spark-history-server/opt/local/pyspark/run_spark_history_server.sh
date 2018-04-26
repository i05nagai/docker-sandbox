#!/bin/bash

/usr/spark-${SPARK_VERSION}/sbin/start-master.sh
/usr/spark-${SPARK_VERSION}/sbin/start-history-server.sh
# not to stop container
tail -f /dev/null
