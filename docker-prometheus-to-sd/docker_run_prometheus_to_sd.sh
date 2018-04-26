#!/bin/bash


docker run \
  --rm -it \
  --user root \
  gcr.io/google-containers/prometheus-to-sd:v0.2.2 \
  /bin/sh
