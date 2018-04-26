FROM ubuntu:16.04

ENV GOPATH=/opt/local/golang
RUN \
    apt-get update \
    && apt-get install -y \
        software-properties-common \
    && add-apt-repository ppa:gophers/archive \
        curl \
        git \
        golang-1.10-go \
    # go dep
    && curl https://raw.githubusercontent.com/golang/dep/master/install.sh | sh
WORKDIR /opt/local/golang
