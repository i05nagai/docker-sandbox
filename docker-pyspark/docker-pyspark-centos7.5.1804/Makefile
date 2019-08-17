NAME = pyspark-centos7.5.1804
PATH_TO_THIS_DIR := $(dir $(realpath $(lastword ${MAKEFILE_LIST})))
PATH_TO_PARENT_DIR := $(dir $(realpath $(PATH_TO_THIS_DIR)))
include ../../script/make/build_docker_image.mk
DOCKER_BUILD_PATH = ..
DOCKER_DOCKERFILE_PATH := Dockerfile

PATH_REPOSITORY := $(shell cd .. && pwd)
DOCKER_NETWORK := pyspark

YARN_PORT := -p 8030:8030
YARN_PORT += -p 8031:8031
YARN_PORT += -p 8032:8032
YARN_PORT += -p 8033:8033
YARN_PORT += -p 8040:8040
YARN_PORT += -p 8042:8042
YARN_PORT += -p 8088:8088

docker-cp:
	mkdir -p spark
	docker cp pyspark-master:/usr/spark-2.4.1/sbin spark
	docker cp pyspark-master:/usr/spark-2.4.1/bin spark
	mkdir -p hadoop
	docker cp pyspark-master:/usr/hadoop/sbin hadoop
	docker cp pyspark-master:/usr/hadoop/bin hadoop
	docker cp pyspark-master:/usr/hadoop/etc hadoop
	docker cp pyspark-master:/usr/hadoop/share hadoop
	docker cp pyspark-master:/usr/hadoop/libexec hadoop

docker-network-create:
	# delete if exists
	docker network rm $(DOCKER_NETWORK) || true
	docker network create $(DOCKER_NETWORK)

docker-network-delete:
	# delete if exists
	docker network rm $(DOCKER_NETWORK) || true

docker-run-master:
	docker run --rm -it \
		--network $(DOCKER_NETWORK) \
		--hostname pyspark-master \
		--name pyspark-master \
		--volume $(PATH_REPOSITORY)/template:/tmp/repository \
		--workdir /tmp/repository/opt \
		$(IMAGE) \
		/bin/bash

docker-exec-master:
	docker exec -it \
		pyspark-master \
		/bin/bash

docker-run-worker:
	docker run --rm -it \
		--network $(DOCKER_NETWORK) \
		--hostname pyspark-worker \
		--name pyspark-worker \
		--volume $(PATH_REPOSITORY)/template:/tmp/repository \
		--workdir /tmp/repository/opt \
		$(IMAGE) \
		/bin/bash
