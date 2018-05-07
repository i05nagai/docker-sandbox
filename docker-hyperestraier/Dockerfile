FROM ubuntu:16.04

RUN \
    apt-get update \
    && apt-get install -y \
        hyperestraier \
        apache2 -y

COPY ./etc /etc
RUN \
    mkdir -p /var/www/cgi-bin /var/www/html \
    && cp /usr/lib/estraier/estseek.cgi /var/www/cgi-bin/ \
    && cp -r /usr/share/hyperestraier/* /var/www/cgi-bin/ \
    && a2dissite 000-default \
    && a2ensite hyperestraier \
    && /etc/init.d/apache2 start \
    && cp -r /usr/share/doc/hyperestraier /var/www/html/doc

RUN estcmd gather -il ja -sd /var/www/casket /var/www/html/doc
