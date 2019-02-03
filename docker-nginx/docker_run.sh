#!/bin/bash

set -x

docker run --rm \
  -it \
  --name nginx \
  --volume $HOME/.local/var/log/nginx:/var/log/nginx \
  --volume $(pwd)/templates/certifications:/etc/ssl:ro \
  -p 8111:80 \
  -p 8443:443 \
  i05nagai/nginx:latest
