#!/bin/bash

FILES="/host/data/data.json"
FILES="${FILES},/host/data/data.csv"
spark-submit \
  --master spark://192.168.10.1:7077 \
  --conf spark.eventLog.enabled=true \
  --conf spark.eventLog.dir=file:///host/spark-events \
  --files ${FILES} \
  /host/load_from_file.py \
  1000 | tee run.log
