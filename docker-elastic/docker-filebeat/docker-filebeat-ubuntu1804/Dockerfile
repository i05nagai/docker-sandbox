FROM ubuntu:18.04

RUN \
    apt-get update \
    # Install Java.
    && apt-get install -y \
        curl \
        gnupg \
        apt-transport-https \
    && curl -L https://artifacts.elastic.co/GPG-KEY-elasticsearch | apt-key add - \
    && echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | tee -a /etc/apt/sources.list.d/elastic-7.x.list \
    && apt-get update \
    && apt-get install -y \
        filebeat


RUN \
    apt-get install -y \
        apt-utils

COPY ./template /
