#!/bin/bash

set -e
set -x

# logrotate --debug /etc/logrotate.conf
logrotate -f /etc/logrotate.conf
