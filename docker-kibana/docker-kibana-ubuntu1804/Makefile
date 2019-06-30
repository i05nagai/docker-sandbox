PATH_TO_THIS_DIR := $(dir $(realpath $(lastword ${MAKEFILE_LIST})))
PATH_TO_PARENT_DIR := $(dir $(realpath $(PATH_TO_THIS_DIR)))
include ../../script/make/build_docker_image.mk
DOCKER_BUILD_PATH = ..
DOCKER_DOCKERFILE_PATH := Dockerfile

docker-network:
	# delete if exists
	docker network rm kibana || true
	docker network create kibana

docker-network-delete:
	# delete if exists
	docker network rm kibana || true

docker-run-elasticsearch:
	docker run \
		--rm \
		-it \
		--workdir /opt/local/elasticsearch \
		--name elasticsearch \
		--network kibana \
		-p 9200:9200 \
		-p 9300:9300 \
		i05nagai/elasticsearch-ubuntu1804:latest \
		/bin/bash

docker-run-kibana:
	docker run \
		--rm \
		-it \
		--workdir /tmp/repository/opt/local/kibana \
		--network kibana \
		--name kibana \
		-p 5601:5601 \
		--volume $(PATH_TO_PARENT_DIR)/template:/tmp/repository \
		$(IMAGE) \
		/bin/bash
