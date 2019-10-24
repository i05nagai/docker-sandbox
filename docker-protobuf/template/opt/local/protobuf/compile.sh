#!/bin/bash

src_dir="."
dist_dir="."

# Generate sample_pb2.py in dist dir
protoc -I=$src_dir --python_out=$dst_dir $src_dir/sample.proto
