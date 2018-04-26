#!/bin/bash

docker run --rm -it \
  --name fluentd \
  --volume $(pwd)/skelton/etc/fluent/config.d:/etc/fluent/config.d \
  i05nagai/fluentd:latest \
  /bin/bash
