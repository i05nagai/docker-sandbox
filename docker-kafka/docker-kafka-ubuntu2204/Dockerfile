FROM ubuntu:22.04

ENV \
    # Define commonly used JAVA_HOME variable
    JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64 \
    KAFKA_VERSION=2.13-3.8.0

ENV \
    KAFKA_HOME=/opt/local/kafka/kafka_${KAFKA_VERSION}

RUN \
    apt-get update \
    # Install Java.
    && apt-get install -y \
        openjdk-8-jdk \
        curl \
    && mkdir -p /opt/local/kafka \
    && cd /opt/local/kafka \
    && curl -L -O https://dlcdn.apache.org/kafka/3.8.0/kafka_${KAFKA_VERSION}.tgz \
    && tar xzf kafka_${KAFKA_VERSION}.tgz \
    && cd kafka_${KAFKA_VERSION}

RUN \
    apt-get install -y \
        vim

ENV \
    PATH=${PATH}:${KAFKA_HOME}/bin
COPY ./template /

RUN \
    apt-get install -y \
        dnsutils \
        netcat
