#!/bin/bash

PATH_THIS_DIR=$(cd $(dirname ${0});pwd)
IMAGE_NAME="i05nagai/jenkins:latest"

docker run \
  --rm -it \
  -p 8080:8080 \
  -p 50000:50000 \
  --name jenkins \
  --volume /var/run/docker.sock:/var/run/docker.sock \
  --privileged \
  --volume ${PATH_THIS_DIR}/samples:/tmp/samples \
  --volume ${PATH_THIS_DIR}/jenkins_home:/var/jenkins_home \
  ${IMAGE_NAME}


