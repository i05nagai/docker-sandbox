#!/bin/bash

set -e

source $SPARK_HOME/sbin/spark-config.sh
source $SPARK_HOME/bin/load-spark-env.sh

export SPARK_MASTER_HOST=`hostname`
export SPARK_MASTER_PORT=7077
export SPARK_MASTER_WEBUI_PORT=8080
export SPARK_MASTER_LOG="/var/log/spark/master/"

mkdir -p $SPARK_MASTER_LOG

ln -sf /dev/stdout $SPARK_MASTER_LOG/spark-master.out

$SPARK_HOME/bin/spark-class \
  org.apache.spark.deploy.master.Master \
  --ip $SPARK_MASTER_HOST \
  --port $SPARK_MASTER_PORT \
  --webui-port $SPARK_MASTER_WEBUI_PORT \
  >> $SPARK_MASTER_LOG/spark-master.out
