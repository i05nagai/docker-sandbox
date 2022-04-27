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

#
# SPARK
#
ENV SPARK_VERSION=3.2.1
# ENV SPARK_HOME=/usr/spark-$SPARK_VERSION
ENV PYSPARK_PYTHON=python3
ENV SPARK_DIST_CLASSPATH="$HADOOP_HOME/etc/hadoop/*:$HADOOP_HOME/share/hadoop/common/lib/*:$HADOOP_HOME/share/hadoop/common/*:$HADOOP_HOME/share/hadoop/hdfs/*:$HADOOP_HOME/share/hadoop/hdfs/lib/*:$HADOOP_HOME/share/hadoop/hdfs/*:$HADOOP_HOME/share/hadoop/yarn/lib/*:$HADOOP_HOME/share/hadoop/yarn/*:$HADOOP_HOME/share/hadoop/mapreduce/lib/*:$HADOOP_HOME/share/hadoop/mapreduce/*:$HADOOP_HOME/share/hadoop/tools/lib/*"

CMD ["bin/spark-class", "org.apache.spark.deploy.master.Master"]

COPY ./template /
RUN PYSPARK_HADOOP_VERSION=3.2 pip3 install pyspark -v
RUN pip3 install -r /opt/local/pyspark-pytest/requirements.txt
# ENV PYTHONPATH="$SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.7-src.zip"
