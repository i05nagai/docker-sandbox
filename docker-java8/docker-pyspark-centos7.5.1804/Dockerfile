FROM centos:centos7.5.1804

ENV \
  # Define commonly used JAVA_HOME variable
  JAVA_HOME=/usr/lib/jvm/java-1.8.0-openjdk-1.8.0.201.b09-2.el7_6.x86_64

RUN \
    yum update \
    # Install Java.
    && yum install -y \
        java-1.8.0-openjdk-devel
