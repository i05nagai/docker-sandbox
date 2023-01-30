FROM ubuntu:16.04
MAINTAINER i05nagai

# add our user and group first to make sure their IDs get assigned consistently, regardless of whatever dependencies get added
RUN \
    groupadd -r mysql \
    && useradd -r -g mysql mysql \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        gnupg \
        dirmngr \
    && rm -rf /var/lib/apt/lists/*

ENV MYSQL_MAJOR=5.7 \
    MYSQL_VERSION=5.7.21-0ubuntu0.16.04.1

# Install MySQL.
RUN \
  apt-get update \
  && DEBIAN_FRONTEND=noninteractive apt-get install -y \
      mysql-server \
  && rm -rf /var/lib/apt/lists/* \
  && sed -i 's/^\(log_error\s.*\)/# \1/' /etc/mysql/mysql.conf.d/mysqld.cnf \
  && echo "mysqld_safe &" > /tmp/config \
  && echo "mysqladmin --silent --wait=30 ping || exit 1" >> /tmp/config \
  && echo "mysql -e 'GRANT ALL PRIVILEGES ON *.* TO \"root\"@\"%\" WITH GRANT OPTION;'" >> /tmp/config \
  && bash /tmp/config \
  && rm -f /tmp/config

EXPOSE 3306
