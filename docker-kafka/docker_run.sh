#!/bin/bash

# tar -xzf kafka_2.11-2.0.0.tgz

docker run -it \
  --rm \
  --volume $(pwd)/script:/opt/kafka/kafka_2.11-2.0.0/script \
  --workdir /opt/kafka/kafka_2.11-2.0.0 \
  --name kafka \
  -p 2181:2181 \
  i05nagai/kafka:latest \
  /bin/bash
