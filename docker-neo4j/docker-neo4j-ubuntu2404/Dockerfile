FROM ubuntu:24.04
MAINTAINER i05nagai

RUN \
    apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get install -y \
        curl \
        apt-transport-https \
        ca-certificates \
        gnupg 

ENV \
    NEO4J_HOME=/usr/bin


RUN \
    curl -fssL https://debian.neo4j.com/neotechnology.gpg.key | gpg --dearmor -o /etc/apt/keyrings/neotechnology.gpg \
    && echo 'deb [signed-by=/etc/apt/keyrings/neotechnology.gpg] https://debian.neo4j.com stable latest' | tee -a /etc/apt/sources.list.d/neo4j.list \
    && apt-get update \
    && apt-get install -y \
        "neo4j=1:2025.01.0"

COPY ./template /
