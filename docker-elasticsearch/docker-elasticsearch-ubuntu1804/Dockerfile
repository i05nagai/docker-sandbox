FROM ubuntu:18.04

ENV \
  # Define commonly used JAVA_HOME variable
  JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64

RUN \
    apt-get update \
    # Install Java.
    && apt-get install -y \
        openjdk-8-jdk

RUN \
    apt-get update \
    && apt-get install -y \
        curl \
        gnupg \
        apt-transport-https \
    && curl -L https://artifacts.elastic.co/GPG-KEY-elasticsearch | apt-key add - \
    && echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | tee -a /etc/apt/sources.list.d/elastic-7.x.list \
    && apt-get update \
    && apt-get install -y \
        elasticsearch

RUN \
    apt-get install -y \
        vim

RUN \
    apt-get update \
    && apt-get install -y \
        apt-utils \
        sudo

COPY ./template /

RUN \
    chown -R elasticsearch:elasticsearch /etc/elasticsearch \
    && chown -R elasticsearch:elasticsearch /usr/share/elasticsearch \
    && chown -R elasticsearch:elasticsearch /usr/share/elasticsearch \
    && chown -R elasticsearch:elasticsearch /var/log/elasticsearch
