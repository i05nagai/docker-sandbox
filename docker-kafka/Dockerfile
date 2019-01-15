FROM ubuntu:16.04

ENV \
    # Define commonly used JAVA_HOME variable
    JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64 \
    KAFKA_VERSION=2.11-2.0.0

ENV \
    KAFKA_HOME=/opt/kafka/kafka_${KAFKA_VERSION}

RUN \
    apt-get update \
    # Install Java.
    && apt-get install -y \
        openjdk-8-jdk \
        curl \
    && mkdir -p /opt/kafka \
    && cd /opt/kafka \
    && curl -L -O http://ftp.jaist.ac.jp/pub/apache/kafka/2.0.0/kafka_${KAFKA_VERSION}.tgz \
    && tar xzf kafka_${KAFKA_VERSION}.tgz \
    && cd kafka_${KAFKA_VERSION}

RUN \
    apt-get install -y \
        vim
