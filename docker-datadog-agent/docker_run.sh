#!/bin/bash

docker run --rm -it \
  --env DD_API_KEY_FILE="" \
  --name datadog-agent \
  i05nagai/datadog-agent \
  /bin/bash
