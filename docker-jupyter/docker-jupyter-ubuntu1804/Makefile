PATH_TO_THIS_DIR := $(dir $(realpath $(lastword ${MAKEFILE_LIST})))
PATH_TO_PARENT_DIR := $(dir $(realpath $(PATH_TO_THIS_DIR)))
include ../../script/make/build_docker_image.mk
DOCKER_BUILD_PATH = ..
DOCKER_DOCKERFILE_PATH := Dockerfile


docker-run:
	docker run --rm -it \
		--network openldap \
		--workdir /tmp/repository/opt/local/jupyter \
		--volume $(PATH_TO_PARENT_DIR)/template:/tmp/repository \
		--name jupyter \
		-p 9999:8000 \
		$(IMAGE) \
		/bin/bash
