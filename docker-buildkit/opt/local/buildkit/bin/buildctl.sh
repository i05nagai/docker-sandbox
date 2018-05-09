#!/bin/bash

set -e

readonly PATH_TO_DOCKERFILE=$1
if [ -z ${PATH_TO_DOCKERFILE+x} ]; then
  echo "Error!"
  exit 1
fi

readonly PATH_TO_DOCKERFILE_DIR=$(dirname ${PATH_TO_DOCKERFILE})
buildctl build \
  --frontend=dockerfile.v0 \
  --local context=${PATH_TO_DOCKERFILE_DIR} \
  --local dockerfile=${PATH_TO_DOCKERFILE_DIR}
