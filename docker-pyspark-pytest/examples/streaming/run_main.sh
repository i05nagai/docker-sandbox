#!/bin/bash


PATH_THIS_DIR=$(cd $(dirname ${0});pwd)
cd ${PATH_THIS_DIR}

spark-submit \
  --master "yarn" \
  --py-files streaming/processor.py,streaming/transform.py,streaming/util.py,streaming/constant.py \
  --deploy-mode client \
    main.py

# --files  
# --py-files pythonfiles.py
# --conf "spark.executor.extraJavaOptions=-Djava.security.auth.login.config=./staging-jaas.conf" 
# --driver-java-options "-Djava.security.auth.login.config=./staging-jaas.conf" 
