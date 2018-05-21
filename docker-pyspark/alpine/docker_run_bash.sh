#!/bin/bash

SCRIPT_DIR=$(cd $(dirname ${0});pwd)
REPOSITORY_DIR=${SCRIPT_DIR}
REPOSITORY_DIRNAME=$(basename $REPOSITORY_DIR)

docker run -it \
  --rm \
  --name pyspark \
  --volume $REPOSITORY_DIR/host:/host \
  --workdir /tmp/$REPOSITORY_DIRNAME \
  i05nagai/pyspark-pytest /bin/bash
