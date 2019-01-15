#!/bin/bash

docker exec -it \
  --workdir /opt/kafka/kafka_2.11-2.0.0 \
  kafka \
  /bin/bash
