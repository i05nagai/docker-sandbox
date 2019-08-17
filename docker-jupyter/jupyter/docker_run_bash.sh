#!/bin/bash

docker run --rm -it \
  --name jupyter \
  --volume $(pwd)/skelton:/host \
  -p 8888:8888 \
  i05nagai/jupyter:latest \
  /bin/bash
