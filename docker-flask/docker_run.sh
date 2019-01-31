#!/bin/bash

docker run --rm -it \
  --name flask \
  --volume $(pwd)/opt:/tmp/opt \
  --workdir /tmp/opt/flask \
  i05nagai/flask:latest \
  /bin/bash
