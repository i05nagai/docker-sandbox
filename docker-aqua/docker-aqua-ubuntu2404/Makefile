PATH_TO_THIS_DIR := $(dir $(realpath $(lastword ${MAKEFILE_LIST})))
PATH_TO_PARENT_DIR := $(dir $(realpath $(PATH_TO_THIS_DIR)))
include ../../script/make/build_docker_image.mk
DOCKER_BUILD_PATH = ..
DOCKER_DOCKERFILE_PATH := Dockerfile

docker-build-amd64:
	docker build \
		--platform linux/amd64 \
		-t $(IMAGE) \
		-f $(DOCKER_DOCKERFILE_PATH) \
		$(PATH_TO_PARENT_DIR)

docker-run:
	docker run \
		--rm \
		-it \
		--name aqua \
		--hostname aqua \
		--volume $(PATH_TO_PARENT_DIR)/template/:/tmp/repository \
		ubuntu:24.04 \
		/bin/bash
