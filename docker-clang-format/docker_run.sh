#!/bin/bash

docker run --rm -it \
  --volume $(pwd):/tmp/repository \
  --workdir /tmp/repository \
  i05nagai/clang-format:latest
