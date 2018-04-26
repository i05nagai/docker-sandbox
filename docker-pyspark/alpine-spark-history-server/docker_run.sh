#!/bin/bash

docker run --rm \
  --detach \
  -p 18080:18080 \
  --volume $(PWD)/logs:/tmp/spark-events \
  makotonagai/pyspark:spark-history-server \
  /bin/bash /tmp/scripts/run_history_server.sh
