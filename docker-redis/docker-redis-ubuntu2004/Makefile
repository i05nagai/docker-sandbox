PATH_TO_THIS_DIR := $(dir $(realpath $(lastword ${MAKEFILE_LIST})))
PATH_TO_PARENT_DIR := $(dir $(realpath $(PATH_TO_THIS_DIR)))
include ../../script/make/build_docker_image.mk
DOCKER_BUILD_PATH = ..
DOCKER_DOCKERFILE_PATH := Dockerfile

docker-network:
	# delete if exists
	docker network rm redis || true
	docker network create redis

docker-network-delete:
	# delete if exists
	docker network rm redis || true

docker-run:
	docker run \
		--rm \
		-it \
		--workdir /tmp/repository/opt/local/redis \
		--name redis \
		--volume $(PATH_TO_PARENT_DIR)/template/:/tmp/repository \
		$(IMAGE) \
		/bin/bash

docker-run-redis-server:
	docker run \
		--rm \
		-it \
		-p 6379:6379 \
		--name redis-server \
		--network redis \
		--hostname redis-server \
		--workdir /tmp/repository/opt/local/redis \
		--volume $(PATH_TO_PARENT_DIR)/template/:/tmp/repository \
		$(IMAGE) \
		/bin/bash

docker-run-redis-server-attach:
	docker exec -it redis-server /bin/bash

docker-run-redis-client:
	docker run \
		--rm \
		-it \
		--name redis-client \
		--network redis \
		--hostname redis-client \
		--workdir /tmp/repository/opt/local/redis \
		--volume $(PATH_TO_PARENT_DIR)/template/:/tmp/repository \
		$(IMAGE) \
		/bin/bash
