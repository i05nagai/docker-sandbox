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
        openjdk-8-jdk

ENV SWAGGER_VERSION=2.4.2
RUN \
    curl \
        -L http://central.maven.org/maven2/io/swagger/swagger-codegen-cli/${SWAGGER_VERSION}/swagger-codegen-cli-${SWAGGER_VERSION}.jar \
        -o swagger-codegen-cli.jar \
    && java -jar swagger-codegen-cli.jar help

ENV SWAGGER_PATH="/opt/local/swagger"
RUN \
    mkdir -p ${SWAGGER_PATH} \
    && mv swagger-codegen-cli.jar ${SWAGGER_PATH}

RUN \
    echo 'alias swagger-codegen="java -jar ${SWAGGER_PATH}/swagger-codegen-cli.jar"' >> /root/.bashrc

COPY ./template /

WORKDIR ${SWAGGER_PATH}
