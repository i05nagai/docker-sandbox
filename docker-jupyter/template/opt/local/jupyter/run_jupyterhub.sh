#!/bin/bash

set -e
set -x

PATH_THIS_DIR=$(cd $(dirname ${0});pwd)
PATH_LOG_DIR=${PATH_THIS_DIR}/log
mkdir -p ${PATH_LOG_DIR}
touch ${PATH_LOG_DIR}/jupyterhub.log

/etc/init.d/nscd restart

jupyterhub \
  --port=8000 \
  --config=${PATH_THIS_DIR}/jupyterhub_config.py \
  --log-level=DEBUG >> ${PATH_LOG_DIR}/jupyterhub.log
