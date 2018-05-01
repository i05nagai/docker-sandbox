#!/bin/bash

docker run --rm -it \
  --privileged \
  -p 111:111 \
  -p 2049:2049 \
  i05nagai/nfs-server:latest \
  /bin/bash 
