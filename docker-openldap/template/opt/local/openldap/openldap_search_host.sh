#!/bin/bash

ldapsearch \
  -H ldap://localhost:2389 \
  -x \
  -LLL \
  -b dc=example,dc=com 'uid=john' cn gidNumber
