FROM centos:centos7.5.1804

#
# java8
#
ENV \
  # Define commonly used JAVA_HOME variable
    JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.212.b04-0.el7_6.x86_64

RUN \
    yum update -y \
    # Install Java.
    && yum install -y \
        java-1.8.0-openjdk-devel

#
# PYTHON 3
#
# Installing given python3 version
RUN \
    yum install -y https://centos7.iuscommunity.org/ius-release.rpm \
    && yum update -y \
    && yum install -y \
        python36u \
        python36u-libs \
        python36u-devel \
        python36u-pip \
    && pip3.6 install --upgrade pip

#
# HADOOP
#
ENV HADOOP_VERSION=2.7.3
ENV HADOOP_HOME=/usr/hadoop-$HADOOP_VERSION
ENV HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
ENV PATH=$PATH:$HADOOP_HOME/bin
RUN \
    curl --location --retry 3 \
        "http://archive.apache.org/dist/hadoop/common/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz" \
        | gunzip \
        | tar -x -C /usr/ \
    && rm -rf $HADOOP_HOME/share/doc

#
# SPARK
#
ENV SPARK_VERSION=2.4.1

ENV SPARK_PACKAGE=spark-$SPARK_VERSION-bin-hadoop2.7
ENV SPARK_HOME=/usr/spark-$SPARK_VERSION
ENV PYSPARK_PYTHON=python3.6
ENV SPARK_DIST_CLASSPATH="$HADOOP_HOME/etc/hadoop/*:$HADOOP_HOME/share/hadoop/common/lib/*:$HADOOP_HOME/share/hadoop/common/*:$HADOOP_HOME/share/hadoop/hdfs/*:$HADOOP_HOME/share/hadoop/hdfs/lib/*:$HADOOP_HOME/share/hadoop/hdfs/*:$HADOOP_HOME/share/hadoop/yarn/lib/*:$HADOOP_HOME/share/hadoop/yarn/*:$HADOOP_HOME/share/hadoop/mapreduce/lib/*:$HADOOP_HOME/share/hadoop/mapreduce/*:$HADOOP_HOME/share/hadoop/tools/lib/*"
ENV PATH=$PATH:$SPARK_HOME/bin

RUN \
    set -x \
    && curl --location --retry 3 \
        "https://archive.apache.org/dist/spark/spark-$SPARK_VERSION/$SPARK_PACKAGE.tgz" \
        | gunzip \
        | tar x -C /usr/ && \
        mv /usr/$SPARK_PACKAGE $SPARK_HOME \
    && rm -rf $SPARK_HOME/examples $SPARK_HOME/ec2

#
# use pyspark with ipython
#
ENV PYSPARK_DRIVER_PYTHON=ipython3
# ENV PYSPARK_DRIVER_PYTHON_OPTS="notebook"
RUN \
    pip3.6 install ipython


WORKDIR /$SPARK_HOME
CMD ["bin/spark-class", "org.apache.spark.deploy.master.Master"]
