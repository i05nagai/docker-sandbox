FROM ubuntu:16.04

ENV GOPATH=/opt/local/heapster
RUN \
    apt-get update \
    && apt-get install -y \
        software-properties-common \
    && add-apt-repository ppa:gophers/archive \
    && apt-get install -y \
        curl \
        git \
        golang-1.10-go
RUN \
    export PATH=$PATH:/usr/lib/go-1.10/bin \
    && go get -u github.com/golang/dep/cmd/dep
RUN \
    git clone https://github.com/kubernetes/heapster.git /opt/local/heapster/build \
    && cd /opt/local/heapster \
    && make
WORKDIR /opt/local/heapster

