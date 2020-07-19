PATH_TO_THIS_DIR := $(dir $(realpath $(lastword ${MAKEFILE_LIST})))
PATH_TO_PARENT_DIR := $(dir $(realpath $(PATH_TO_THIS_DIR)))
include ../../../script/make/build_docker_image.mk
DOCKER_BUILD_PATH = ..
DOCKER_DOCKERFILE_PATH := Dockerfile

docker-network:
	# delete if exists
	docker network rm kibana || true
	docker network create kibana

docker-network-delete:
	# delete if exists
	docker network rm kibana || true

docker-run-filebeat:
	docker run \
		--rm \
		-it \
		--workdir /tmp/repository/opt/local/filebeat \
		--name filebeat \
		--volume $(PATH_TO_PARENT_DIR)/template:/tmp/repository \
		$(IMAGE) \
		/bin/bash

