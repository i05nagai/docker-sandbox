FROM ubuntu:14.04
MAINTAINER i05nagai

RUN \
    apt-get update \
    && apt-get install -y \
        software-properties-common \

RUN \
    apt-add-repository "deb http://apt.llvm.org/trusty/ llvm-toolchain-trusty main" \
    && apt-get install -y \
        clang-format-5.0
