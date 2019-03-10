#!/bin/bash

docker run --rm -it \
  --volume $(pwd)/example:/tmp/repository \
  --workdir /tmp/repository \
  i05nagai/serverless:latest \
  /bin/bash
