#!/bin/bash

# fluent-bit -c /opt/fluent-bit/config/sample1.conf
fluent-bit \
  --parser=/template/opt/fluent-bit/config/parsers.conf \
  --config=/template/opt/fluent-bit/config/sample2.conf
