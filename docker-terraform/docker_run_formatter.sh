#!/bin/bash

PATH_TO_THIS_DIR=$(cd $(dirname ${0});pwd)

docker run \
  --rm -it \
  --name terraform \
  --volume ${PATH_TO_THIS_DIR}/example:/tmp/example \
  i05nagai/terraform:latest \
  fmt /tmp/example
