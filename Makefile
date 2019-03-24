IGNORE_FILES = README.md
IGNORE_FILES += Makefile
IGNORE_FILES += script
IGNORE_FILES += docker-apache-beam
IGNORE_FILES += docker-cadviser
IGNORE_FILES += docker-heapster
IGNORE_FILES += docker-jupyter
IGNORE_FILES += docker-pyspark
IGNORE_FILES += google-containers
include script/make/build_directory.mk

#
# buildkit
#
buildkit: core

push-buildkit: core

#
# embulk
#
embulk: java8

push-embulk: java8

#
# java8
#
java8: core

push-java8: core

#
# pyspark
#
pyspark: java8

push-pyspark: java8
