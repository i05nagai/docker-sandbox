#!/bin/bash

set -e

if [ -z ${MYSQL_ROOT_PASSWORD+x} ]; then
  exit 1
fi

mysqld -D

mysql -u root -h localhost -P 3306 <<EOL
ALTER USER 'root'@'localhost' IDENTIFIED BY '${MYSQL_ROOT_PASSWORD}';
CREATE DATABASE sample;
CREATE TABLE sample.Samples (
    int_f int,
    varchar_f varchar(255),
    text_f TEXT(10),
    blob_f BLOB(10),
    float_f FLOAT,
    bool_f BOOL,
    bit_f BIT,
    date_f DATE,
    timestmap_f TIMESTAMP,
    json_f JSON
);
EOL


