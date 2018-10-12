#!/bin/bash

tar -xzf kafka_2.11-2.0.0.tgz

docker run -it \
  i05nagai/kafka:latest \
  /bin/bash
