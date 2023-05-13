FROM ubuntu:22.04
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
    MYSQL_VERSION=5.7.21-0ubuntu0.22.04.1 \
    MYSQL_DPKG_FILE=mysql-apt-config_0.8.12-1_all.deb

# Install MySQL.
RUN \
  apt update \
  && apt install -y \
      wget \
      lsb-release \
  && wget -o /tmp/mysql-apt-config_0.8.12-1_all.deb https://dev.mysql.com/get/mysql-apt-config_0.8.12-1_all.deb \
  && dpkg -i /tmp/mysql-apt-config_0.8.12-1_all.deb \
  && DEBIAN_FRONTEND=noninteractive apt-get install -y \
      mysql-server="${MYSQL_VERSION}" \
  && rm -rf /var/lib/apt/lists/* \
  && sed -i 's/^\(log_error\s.*\)/# \1/' /etc/mysql/mysql.conf.d/mysqld.cnf \
  && echo "mysqld_safe &" > /tmp/config \
  && echo "mysqladmin --silent --wait=30 ping || exit 1" >> /tmp/config \
  && echo "mysql -e 'GRANT ALL PRIVILEGES ON *.* TO \"root\"@\"%\" WITH GRANT OPTION;'" >> /tmp/config \
  && bash /tmp/config \
  && rm -f /tmp/config

EXPOSE 3306
