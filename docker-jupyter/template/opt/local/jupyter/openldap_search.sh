#!/bin/bash

ldapsearch \
  -H ldap://openldap:389 \
  -x \
  -LLL \
  -b dc=example,dc=com \
  'uid=john'
