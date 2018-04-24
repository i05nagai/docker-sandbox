#!/bin/bash

docker run \
  --rm -it \
  gcr.io/google_containers/heapster-amd64:v1.5.0 \
  --help
