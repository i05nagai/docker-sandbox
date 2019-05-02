PATH_TO_THIS_DIR := $(dir $(realpath $(lastword ${MAKEFILE_LIST})))
PATH_TO_PARENT_DIR := $(dir $(realpath $(PATH_TO_THIS_DIR)))
include ../../script/make/build_docker_image.mk
DOCKER_BUILD_PATH = ..
DOCKER_DOCKERFILE_PATH := Dockerfile

docker-network:
	# delete if exists
	docker network rm kafka || true
	docker network create kafka

docker-network-delete:
	# delete if exists
	docker network rm kafka || true

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

docker-run-kafka-server:
	docker run \
		--rm \
		-it \
		-p 9092:9092 \
		--name kafka-server \
		--network kafka \
		--hostname kafka-server \
		--workdir /tmp/repository/opt/local/kafka \
		--volume $(PATH_TO_PARENT_DIR)/template/:/tmp/repository \
		$(IMAGE) \
		/bin/bash

docker-run-kafka-client:
	docker run \
		--rm \
		-it \
		--name kafka-client \
		--network kafka \
		--hostname kafka-client \
		--workdir /tmp/repository/opt/local/kafka \
		--volume $(PATH_TO_PARENT_DIR)/template/:/tmp/repository \
		$(IMAGE) \
		/bin/bash

docker-run-kafka-zookeeper:
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
