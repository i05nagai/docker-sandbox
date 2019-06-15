FROM ubuntu:18.04

ENV \
    # Define commonly used JAVA_HOME variable
    JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64

RUN \
    apt-get update \
    # Install Java.
    && apt-get install -y \
        openjdk-8-jdk \
        curl

ENV ZOOKEEPER_VERSION=3.4.9

RUN \
    mkdir -p /opt/local/zookeeper \
    && cd /opt/local/zookeeper \
    && curl -L -O https://archive.apache.org/dist/zookeeper/zookeeper-${ZOOKEEPER_VERSION}/zookeeper-${ZOOKEEPER_VERSION}.tar.gz \
    && tar xzf zookeeper-${ZOOKEEPER_VERSION}.tar.gz \
    && cd zookeeper-${ZOOKEEPER_VERSION}

COPY ./template /
