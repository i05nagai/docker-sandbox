FROM ubuntu:16.04

ENV \
  # Define commonly used JAVA_HOME variable
  JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64

RUN \
    apt-get update \
    # Install Java.
    && apt-get install -y \
        openjdk-8-jdk \
        curl \
    && mkdir -p /opt/kafka \
    && cd /opt/kafka \
    && curl -L -O http://ftp.jaist.ac.jp/pub/apache/kafka/2.0.0/kafka_2.11-2.0.0.tgz \
    && tar xzf kafka_2.11-2.0.0.tgz \
    && cd kafka_2.11-2.0.0
