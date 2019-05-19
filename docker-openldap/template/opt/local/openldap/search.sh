#!/bin/bash

ldapsearch -x -LLL -b dc=example,dc=com 'uid=john' cn gidNumber
