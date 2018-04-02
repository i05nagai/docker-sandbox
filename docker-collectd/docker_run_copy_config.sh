#!/bin/bash

docker run \
  --name collectd \
  -d \
  --rm \
  i05nagai/collectd:latest \
  sleep 40s

sleep 10s
docker cp collectd:/etc/collectd .
