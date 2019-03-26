#!/bin/bash

IMAGE=i05nagai/swagger:latest

PATH_THIS_DIR=$(cd $(dirname ${0});pwd)

docker run --rm -it \
  --volume ${PATH_THIS_DIR}/examples:/tmp/examples \
  --workdir /tmp/examples \
  ${IMAGE} \
  /bin/bash
