#!/bin/bash

# check connectivity
ldapsearch \
  -H ldap://openldap:389 \
  -x \
  -LLL \
  -b dc=example,dc=com \
  'uid=john'
# ldapsearch -H ldap://openldap:389 -x -LLL -b dc=example,dc=com 'uid=john' cn gidNumber
# ldapsearch -H ldap://openldap:389 -b dc=example,dc=com -x uid=i05nagai
