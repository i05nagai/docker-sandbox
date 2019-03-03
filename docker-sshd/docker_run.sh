#!/bin/bash

set -e

GITHUB_USER_NAME=$1

docker run --rm -it \
  --name sshd \
  --volume $(pwd)/skelton:/host \
  --env HOME_USERS="${GITHUB_USER_NAME}:" \
  --env HOME_SUDOERS="${GITHUB_USER_NAME}" \
  -p 1122:22 \
  i05nagai/sshd:latest \
  /usr/sbin/sshd -D
