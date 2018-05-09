#!/bin/bash

set -e
set -x

PATH_TO_THIS_DIR=$(cd $(dirname ${0});pwd)
BUILDER_DOCKER_PREFIX=i05nagai/

if [ -z `docker volume ls --filter name=docker --quiet` ]; then
  docker volume create docker
fi

if [ -z `docker ps --filter name=docker --quiet` ]; then
  docker run \
    --rm -it \
    --privileged \
    --name docker \
    --volume docker:/var/lib/docker \
    -d \
    docker:dind
fi

docker run \
  --rm -it \
  --name buildkit \
  --link docker \
  --env DOCKER_HOST=tcp://docker:2375 \
  --volume ${PATH_TO_THIS_DIR}:/tmp/host \
  ${BUILDER_DOCKER_PREFIX}buildkit:latest \
  /bin/bash

if [ ! -z `docker ps --filter name=docker --quiet` ]; then
  docker kill docker
fi

if [ ! -z `docker volume ls --filter name=docker --quiet` ]; then
  # docker volume rm docker
  echo "Volume still exists."
fi
