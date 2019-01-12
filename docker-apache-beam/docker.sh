#!/bin/bash

docker run --rm \
  -it \
  -v $(pwd):/tmp/repository \
  --workdir /tmp/repository \
  i05nagai/apache-beam-python2:latest \
  /bin/bash
