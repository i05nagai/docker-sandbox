FROM ubuntu:16.04

ENV \
    PROTOBUF_VERSION=3.2.0

RUN \
    apt-get update \
    # Install Java.
    && apt-get install -y \
        curl \
        zip \
    && mkdir -p /opt/local/protobuf \
    && cd /opt/local/protobuf \
    && curl -OL https://github.com/google/protobuf/releases/download/v${PROTOBUF_VERSION}/protoc-${PROTOBUF_VERSION}-linux-x86_64.zip \
    && unzip protoc-${PROTOBUF_VERSION}-linux-x86_64.zip -d protoc3 \
    && mv protoc3/bin/* /usr/local/bin/ \
    && mv protoc3/include/* /usr/local/include/ \
    && chown root /usr/local/bin/protoc \
    && chown -R root /usr/local/include/google

ENV \
    PATH=${PATH}

COPY ./template /
