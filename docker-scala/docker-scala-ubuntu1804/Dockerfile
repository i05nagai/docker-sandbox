FROM ubuntu:18.04

ENV \
  # Define commonly used JAVA_HOME variable
  JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64

RUN \
    apt-get update \
    # Install Java.
    && apt-get install -y \
        openjdk-8-jdk \
        scala
