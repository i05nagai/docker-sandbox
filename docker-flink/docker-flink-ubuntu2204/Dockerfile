FROM ubuntu:22.04

RUN \
    apt-get update \
    # Install Java.
    && apt-get install -y \
        openjdk-11-jdk \
        curl

ENV FLINK_HOME=/opt/flink
ENV FLINK_VERSION=1.16.1
ENV FLINK_URL_FILE_PATH=flink/flink-${FLINK_VERSION}/flink-${FLINK_VERSION}-bin-scala_2.12.tgz
ENV FLINK_TGZ_URL=https://www.apache.org/dyn/closer.cgi?action=download&filename=${FLINK_URL_FILE_PATH}
ENV PATH=${FLINK_HOME}/bin:$PATH
# http://apache.mirrors.spacedump.net/flink/flink-1.10.0/flink-1.10.0-bin-scala_2.11.tgz

RUN \
    curl -L ${FLINK_TGZ_URL} -o /tmp/flink-${FLINK_VERSION}-bin-scala_2.12.tgz -o /tmp \
    && tar xzf /tmp/flink-${FLINK_VERSION}-bin-scala_2.12.tgz -C /tmp \
    && mv /tmp/flink-${FLINK_VERSION} ${FLINK_HOME} \
    && rm /tmp/flink-${FLINK_VERSION}-bin-scala_2.12.tgz

#
# gradle
# 
ENV GRADLE_HOME=/opt/gradle
ENV GRADLE_VERSION=6.3
ENV PATH=${GRADLE_HOME}/bin:${PATH}

RUN \
    apt-get update \
    && apt-get install -y \
        zip \
    && curl -L https://services.gradle.org/distributions/gradle-${GRADLE_VERSION}-bin.zip -o /tmp/gradle-${GRADLE_VERSION}-bin.zip \
    && unzip /tmp/gradle-${GRADLE_VERSION}-bin.zip -d /tmp \
    && mv /tmp/gradle-${GRADLE_VERSION} ${GRADLE_HOME} \
    && rm /tmp/gradle-${GRADLE_VERSION}-bin.zip

#
# scala
#
ENV SCALA_VERSION=2.12.10
RUN \
    curl -s "https://get.sdkman.io" | bash \
    && bash -c "source \"$HOME/.sdkman/bin/sdkman-init.sh\" && sdk install scala ${SCALA_VERSION} && sdk install sbt"

