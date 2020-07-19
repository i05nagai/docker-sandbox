FROM ubuntu:18.04

ENV \
  # Define commonly used JAVA_HOME variable
  JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64

RUN \
    apt-get update \
    # Install Java.
    && apt-get install -y \
        openjdk-8-jdk


ENV GRADLE_HOME=/opt/gradle
ENV GRADLE_VERSION=6.3
ENV PATH=${GRADLE_HOME}/bin:${PATH}

RUN \
    apt-get update \
    && apt-get install -y \
        curl \
        zip \
    && curl -L https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip -o /tmp/gradle-${GRADLE_VERSION}-bin.zip \
    && unzip /tmp/gradle-${GRADLE_VERSION}-bin.zip -d /tmp \
    && mv /tmp/gradle-${GRADLE_VERSION} ${GRADLE_HOME} \
    && rm /tmp/gradle-${GRADLE_VERSION}-bin.zip
