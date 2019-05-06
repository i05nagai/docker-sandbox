PATH_TO_THIS_DIR := $(dir $(realpath $(lastword ${MAKEFILE_LIST})))
PATH_TO_PARENT_DIR := $(dir $(realpath $(PATH_TO_THIS_DIR)))
include ../../script/make/build_docker_image.mk
DOCKER_BUILD_PATH = ..
DOCKER_DOCKERFILE_PATH := Dockerfile

docker-run:
	docker run \
		--rm \
		-it \
		--workdir /tmp/repository/opt/local/kafka \
		--network kafka \
		--name kafka-server \
		--volume $(PATH_TO_PARENT_DIR)/template/:/tmp/repository \
		$(IMAGE) \
		/bin/bash

docker-kafka-server:
	docker run \
		--rm \
		-it \
		--network kafka \
		--name kafka-server \
		--hostname kafka-server \
		--workdir /tmp/repository/opt/local/kafka \
		--volume $(PATH_TO_PARENT_DIR)/template/:/tmp/repository \
		$(IMAGE) \
		/bin/bash

docker-kafka-zookeeper:
	docker run \
		--rm \
		-it \
		-p 2181:2181 \
		--network kafka \
		--name kafka-zookeeper \
		--hostname kafka-zookeeper \
		--workdir /tmp/repository/opt/local/kafka \
		--volume $(PATH_TO_PARENT_DIR)/template/:/tmp/repository \
		$(IMAGE) \
		/bin/bash

