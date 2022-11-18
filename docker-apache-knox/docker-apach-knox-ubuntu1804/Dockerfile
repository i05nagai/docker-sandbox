FROM ubuntu:18.04

#
# java8
#
ENV \
  # Define commonly used JAVA_HOME variable
  JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64

RUN \
    apt-get update \
    # Install Java.
    && apt-get install -y \
        curl \
        binutils \
        openjdk-8-jdk

#
# HADOOP
#
ENV HADOOP_VERSION=3.3.2
ENV HADOOP_HOME=/usr/hadoop
ENV HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
ENV PATH=$PATH:$HADOOP_HOME/bin
RUN \
    curl --location --retry 3 \
        "http://archive.apache.org/dist/hadoop/common/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz" \
        | gunzip \
        | tar -x -C /usr/ \
    && mv /usr/hadoop-$HADOOP_VERSION /usr/hadoop \
    && rm -rf $HADOOP_HOME/share/doc

RUN \
    apt-get update \
    # Install Java.
    && apt-get install -y \
        unzip

ENV KNOX_VERSION=1.6.0
ENV KNOX_HOME=/usr/knox

RUN \
    curl --location --retry 3 \
        -o /tmp/knox-${KNOX_VERSION}.zip \
        "https://dlcdn.apache.org/knox/${KNOX_VERSION}/knox-${KNOX_VERSION}.zip" \
    && unzip /tmp/knox-${KNOX_VERSION}.zip -d ${KNOX_HOME} \
    && rm -rf /tmp/knox-${KNOX_VERSION}.zip

RUN \
    groupadd -g 10000 i05nagai \
    && useradd -u 10000 -g i05nagai -s /bin/sh i05nagai

USER i05nagai
