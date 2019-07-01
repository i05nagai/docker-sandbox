#!/bin/bash

set -e

/etc/init.d/nscd restart
/usr/sbin/sshd -D
# /usr/sbin/sshd -D -d -d -d
