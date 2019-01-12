#!/bin/bash

set -x

PATH_TO_THIS_DIR=$(cd $(dirname ${0});pwd)
export PYTHONPATH=${PATH_TO_THIS_DIR}

# python2.7 -m example/simple
# python2.7 -m example/join/simple_join

# python2.7 -m example/filter/simple_filter
# python2.7 -m example/filter/filters

# python2.7 -m example/simple_group_by
# python2.7 -m example/group_by/unique


# python2.7 -m example/wordcount

# python2.7 -m example/io/simple_read_write

# python2.7 -m example/combine/simple_combine
# python2.7 -m example/combine/average

python2.7 -m example/flatten/simple_flatten

# python2.7 -m example/partition/simple_partition

# python2.7 -m example/side_input/simple_side_input

# python2.7 -m example/window/simple_window
