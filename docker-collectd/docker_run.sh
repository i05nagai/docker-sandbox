#!/bin/bash

docker run \
  --name collectd \
  --rm -it \
  i05nagai/collectd:latest \
  /bin/bash
