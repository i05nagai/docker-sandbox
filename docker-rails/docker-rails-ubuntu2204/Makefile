PATH_TO_THIS_DIR := $(dir $(realpath $(lastword ${MAKEFILE_LIST})))
PATH_TO_PARENT_DIR := $(dir $(realpath $(PATH_TO_THIS_DIR)))
include ../../script/make/build_docker_image.mk
DOCKER ?= docker
DOCKER_BUILD_PATH = ..
DOCKER_DOCKERFILE_PATH := Dockerfile

docker-run:
	$(DOCKER) run \
		--rm \
		-it \
		--workdir /opt/rails \
		--name rails \
		--volume $(PATH_TO_PARENT_DIR)/template:/tmp/repository \
		-p 3000:3000 \
		i05nagai/rails-ubuntu2204:latest \
		/bin/bash
