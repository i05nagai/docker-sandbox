#!/bin/bash

docker run --rm -it \
  --name jupyter \
  --volume $(pwd)/templates:/host \
  i05nagai/jupyter:latest \
  /bin/bash
