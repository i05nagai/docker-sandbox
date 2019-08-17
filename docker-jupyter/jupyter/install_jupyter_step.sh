#!/bin/bash

cluster_id='j-....'

aws emr add-steps \
    --cluster-id ${cluster_id} \
    --steps Type=CUSTOM_JAR,Name=CustomJAR,ActionOnFailure=CONTINUE,Jar=s3://ap-northeast-1.elasticmapreduce/libs/script-runner/script-runner.jar,Args=["s3://aws-bigdata-blog/artifacts/aws-blog-emr-jupyter/install-jupyter-emr5.sh","--python3","--toree","--ds-packages","--python-packages","'ggplot nilearn'","--ml-packages","--cached-install","--notebook-dir","s3://path/to/jupyter_notebook/","--port","8080","--jupyterhub-port","8001","--copy-samples"]
