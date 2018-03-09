#!/bin/bash

set -x

docker run --rm \
  -it \
  --name nginx \
  -p 8111:80 \
  -p 8443:443 \
  -v $(pwd)/certifications:/etc/ssl:ro \
  i05nagai/nginx:latest
