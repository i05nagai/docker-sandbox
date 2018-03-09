FROM ubuntu:16.10

RUN apt-get update
RUN apt-get install hyperestraier -y
RUN apt-get install apache2 -y

COPY ./etc /
RUN mkdir -p /var/www/cgi-bin /var/www/html
RUN cp /usr/lib/estraier/estseek.cgi /var/www/cgi-bin/
RUN cp -r /usr/share/hyperestraier/* /var/www/cgi-bin/
RUN a2dissite 000-default
RUN a2ensite hyperestraier
RUN /etc/init.d/apache2 start

RUN cp -r /usr/share/doc/hyperestraier /var/www/html/doc
RUN estcmd gather -il ja -sd /var/www/casket /var/www/html/doc
