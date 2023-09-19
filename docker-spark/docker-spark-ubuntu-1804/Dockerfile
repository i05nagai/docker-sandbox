FROM ubuntu:18.04

#
# java8
#
ENV \
  # Define commonly used JAVA_HOME variable
  JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64

RUN \
    apt-get update \
    # Install Java.
    && apt-get install -y \
        openjdk-11-jdk \
        maven

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
ENV HADOOP_VERSION=2.10.2
ENV HADOOP_HOME=/usr/hadoop
ENV HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
ENV PATH=$PATH:$HADOOP_HOME/bin

RUN \
    curl --location --retry 3 \
        "https://dlcdn.apache.org/hadoop/common/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz" \
        | gunzip \
        | tar -x -C /usr/ \
    && mv /usr/hadoop-$HADOOP_VERSION /usr/hadoop \
    && rm -rf $HADOOP_HOME/share/doc

#
# SPARK
#
ENV SPARK_VERSION=3.4.1
ENV SPARK_PACKAGE=spark-$SPARK_VERSION-bin-without-hadoop
ENV SPARK_HOME=/usr/spark-$SPARK_VERSION
ENV PYSPARK_PYTHON=python3
ENV SPARK_DIST_CLASSPATH="$HADOOP_HOME/etc/hadoop/*:$HADOOP_HOME/share/hadoop/common/lib/*:$HADOOP_HOME/share/hadoop/common/*:$HADOOP_HOME/share/hadoop/hdfs/*:$HADOOP_HOME/share/hadoop/hdfs/lib/*:$HADOOP_HOME/share/hadoop/hdfs/*:$HADOOP_HOME/share/hadoop/yarn/lib/*:$HADOOP_HOME/share/hadoop/yarn/*:$HADOOP_HOME/share/hadoop/mapreduce/lib/*:$HADOOP_HOME/share/hadoop/mapreduce/*:$HADOOP_HOME/share/hadoop/tools/lib/*"
ENV PATH=$PATH:$SPARK_HOME/bin

RUN \
    curl --location --retry 3 \
        "https://dlcdn.apache.org/spark/spark-$SPARK_VERSION/$SPARK_PACKAGE.tgz" \
        | gunzip \
        | tar x -C /usr/ \
    && mv /usr/$SPARK_PACKAGE $SPARK_HOME \
    && rm -rf $SPARK_HOME/examples $SPARK_HOME/ec2

WORKDIR /$SPARK_HOME
CMD ["bin/spark-class", "org.apache.spark.deploy.master.Master"]
