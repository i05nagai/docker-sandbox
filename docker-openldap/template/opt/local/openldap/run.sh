#!/bin/bash

set -x

dpkg-reconfigure -f noninteractive slapd
slapd
