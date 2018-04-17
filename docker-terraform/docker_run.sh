#!/bin/bash

docker run \
  --rm -it \
  --name terraform \
  i05nagai/terraform:latest \
  terraform --help
