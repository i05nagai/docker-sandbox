IGNORE_FILES=README.md Makefile script google-containers docker-pyspark docker-jupyter docker-cadviser
include script/make/build_directory.mk

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
