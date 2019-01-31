#!/bin/bash

docker run --rm -it \
  --name flask \
  --volume $(pwd)/opt:/tmp/opt \
  --workdir /tmp/opt/flask \
  -p 8080:5000 \
  i05nagai/flask:latest \
  /bin/bash
