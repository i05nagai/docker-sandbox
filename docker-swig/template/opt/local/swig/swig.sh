#!/bin/bash

set -x
set -e

OBJS=`ls cpp/*.cc`
swig -c++ -cppext cc -python  -outdir python cpp/example.i
c++ -fPIC -I /usr/include/python3.6 -c -o cpp/example_wrap.o cpp/example_wrap.cc
c++ -fPIC -I /usr/include/python3.6 cpp/example_wrap.o ${OBJS} -o cpp/example.so
