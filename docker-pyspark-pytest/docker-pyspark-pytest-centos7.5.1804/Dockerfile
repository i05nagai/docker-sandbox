ARG DOCKER_IMAGE_PREFIX
FROM ${DOCKER_IMAGE_PREFIX}pyspark-centos7.5.1804:latest

COPY ./template/opt/local/pyspark-pytest/requirements.txt /opt/local/pyspark-pytest/requirements.txt
RUN pip install -r /opt/local/pyspark-pytest/requirements.txt
ENV PYTHONPATH="$SPARK_HOME/python:$SPARK_HOME/python/lib/py4j-0.10.7-src.zip"
COPY ./template /
