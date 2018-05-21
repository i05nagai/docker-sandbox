FROM i05nagai/pyspark-alpine:latest

# GENERAL DEPENDENCIES
RUN \
    apk update \
    && apk add zip

# PYTHON DEPENDENCIES
COPY requirements.txt /etc/requirements.txt
RUN \
    pip install -r /etc/requirements.txt \
    && rm /etc/requirements.txt
COPY ./skelton /
