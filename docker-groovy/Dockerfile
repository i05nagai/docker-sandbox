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

RUN \
    apt-get install -y \
        zip \
    && curl -s get.sdkman.io | bash \
    # source cannot use with /bin/sh
    && /bin/bash -c "source /root/.sdkman/bin/sdkman-init.sh && sdk install groovy"
