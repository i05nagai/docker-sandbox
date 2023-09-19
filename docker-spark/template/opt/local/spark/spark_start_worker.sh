#!/bin/bash

set -e

source $SPARK_HOME/sbin/spark-config.sh
source $SPARK_HOME/bin/load-spark-env.sh

export SPARK_WORKER_LOG="/var/log/spark/worker/"
export SPARK_WORKER_WEBUI_PORT=8081
export SPARK_MASTER="spark://pyspark-pytest-master:7077"

mkdir -p $SPARK_WORKER_LOG

ln -sf /dev/stdout $SPARK_WORKER_LOG/spark-worker.out

$SPARK_HOME/bin/spark-class \
  org.apache.spark.deploy.worker.Worker \
  --webui-port $SPARK_WORKER_WEBUI_PORT $SPARK_MASTER \
  >> $SPARK_WORKER_LOG/spark-worker.out
