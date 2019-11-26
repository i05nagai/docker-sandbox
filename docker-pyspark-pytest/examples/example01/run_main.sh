#!/bin/bash


PATH_THIS_DIR=$(cd $(dirname ${0});pwd)
cd ${PATH_THIS_DIR}

spark-submit \
  --master "yarn" \
  --py-files projectname/util.py,projectname/wordcount.py \
  --deploy-mode client \
    projectname/wordcount_use.py

# --files  
# --py-files pythonfiles.py
# --conf "spark.executor.extraJavaOptions=-Djava.security.auth.login.config=./jaas.conf" 
# --driver-java-options "-Djava.security.auth.login.config=./jaas.conf" 

