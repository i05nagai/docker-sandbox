PATH_TO_THIS_DIR := $(dir $(realpath $(lastword ${MAKEFILE_LIST})))
PATH_TO_PARENT_DIR := $(dir $(realpath $(PATH_TO_THIS_DIR)))
include ../../script/make/build_docker_image.mk
DOCKER_BUILD_PATH = ..
DOCKER_DOCKERFILE_PATH := Dockerfile

docker-network:
	# delete if exists
	docker network rm openldap || true
	docker network create openldap

docker-network-delete:
	# delete if exists
	docker network rm openldap || true

docker-run:
	docker run --rm -it \
		--name openldap \
		--network "openldap" \
		--hostname openldap \
		-p 8888:80 \
		-p 2389:389 \
		-p 2636:636 \
		--volume $(PATH_TO_PARENT_DIR)/template:/tmp/repository \
		--workdir /tmp/repository \
		${IMAGE} /bin/bash
