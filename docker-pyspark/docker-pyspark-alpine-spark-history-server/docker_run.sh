#!/bin/bash

PATH_TO_THIS_DIR=$(cd $(dirname ${0});pwd)

docker run --rm \
  -p 18080:18080 \
  --name pyspark \
  --detach \
  --volume ${PATH_TO_THIS_DIR}/logs:/tmp/spark-events \
  i05nagai/pyspark-alpine-spark-history-server \
  /bin/bash /opt/local/pyspark/run_spark_history_server.sh
