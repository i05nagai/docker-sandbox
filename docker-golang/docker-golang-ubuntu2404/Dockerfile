FROM ubuntu:24.04

RUN \
    apt-get update

RUN \
    apt-get install -y \
        build-essential \
        software-properties-common

ENV GOVERSION=1.24
RUN \
    add-apt-repository ppa:longsleep/golang-backports \
    && apt-get update \
    && apt-get install -y \
        curl \
        git \
        golang-${GOVERSION}

ENV GOPATH=/opt/local/golang
ENV PATH=$PATH:${GOPATH}/bin:/usr/lib/go-${GOVERSION}/bin
RUN \
    mkdir -p $GOPATH/bin

RUN go install github.com/golangci/golangci-lint/v2/cmd/golangci-lint@v2.3.0
