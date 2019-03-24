#!/bin/bash

set -e
set -x

PATH_THIS_DIR=$(cd $(dirname ${0});pwd)

${SWAGGER_PATH}/entrypoint.sh \
  generate \
  --lang python \
  --output ${PATH_THIS_DIR}/code \
  -i ${PATH_THIS_DIR}/sample-petstore.yaml
