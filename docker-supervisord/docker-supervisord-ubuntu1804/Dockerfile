FROM ubuntu:18.04
MAINTAINER i05nagai

RUN apt-get update \
    && apt-get install -y \
        supervisor \
        logrotate \
        rsyslog \
    && mkdir -p /var/log/supervisor

WORKDIR /opt/local/supervisord
COPY ./templates /
ENTRYPOINT ["/opt/local/supervisord/entrypoint.sh"]
