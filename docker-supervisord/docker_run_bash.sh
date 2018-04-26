#!/bin/bash

docker run --rm -it \
  --name supervisord \
  --volume $(pwd)/templates:/host \
  i05nagai/supervisord:latest \
  /bin/bash
