FROM ubuntu:16.04
MAINTAINER i05nagai

RUN apt-get update \
    && apt-get install -y \
        supervisor \
        logrotate \
    && mkdir -p /var/log/supervisor

COPY ./templates /
WORKDIR /opt/local/supervisord
ENTRYPOINT ["/opt/local/supervisord/entrypoint.sh"]
