#!/bin/bash

set -e

PATH_THIS_DIR=$(cd $(dirname ${0});pwd)
mkdir -p ${PATH_THIS_DIR}
touch ${PATH_THIS_DIR}/jupyterhub.log

jupyterhub \
  --port=8000 \
  --config=${PATH_THIS_DIR}/jupyterhub_config.py \
  --log-level=DEBUG >> ${PATH_THIS_DIR}/jupyterhub.log
