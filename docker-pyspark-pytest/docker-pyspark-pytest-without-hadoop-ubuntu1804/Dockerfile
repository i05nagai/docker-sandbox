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
        openjdk-8-jdk

#
# PYTHON 3
#
# Installing given python3 version
RUN \
    apt-get update \
    && apt-get install -y \
        python3.8 \
        curl \
        python3-pip \
    && pip3 install --upgrade pip==9.0.1

#
# SPARK
#
ENV PYSPARK_PYTHON=python3
CMD ["bin/spark-class", "org.apache.spark.deploy.master.Master"]
COPY ./template /
RUN PYSPARK_HADOOP_VERSION=3.2 pip3 install pyspark -v
RUN pip3 install -r /opt/local/pyspark-pytest/requirements.txt
