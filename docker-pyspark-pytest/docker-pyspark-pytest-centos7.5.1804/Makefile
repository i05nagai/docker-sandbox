NAME = pyspark-pytest-centos7.5.1804
include ../../script/make/build_docker_image.mk

DOCKER_DOCKERFILE_PATH = Dockerfile
DOCKER_BUILD_PATH = ..
DOCKER_NETWORK := pyspark-pytest

PATH_REPOSITORY := $(shell cd .. && pwd)

docker-run:
	docker run --rm -it \
		--name pyspark-pytest \
		--volume $(PATH_REPOSITORY)/examples:/tmp/examples \
		--workdir /tmp/examples \
		$(IMAGE) \
		/bin/bash

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
		--hostname pyspark-pytest-master \
		--name pyspark-pytest-master \
		--volume $(PATH_REPOSITORY)/examples:/tmp/examples \
		--workdir /tmp/examples \
		$(IMAGE) \
		/bin/bash

docker-exec-master:
	docker exec -it \
		pyspark-pytest-master \
		/bin/bash

docker-run-worker:
	docker run --rm -it \
		--network $(DOCKER_NETWORK) \
		--hostname pyspark-pytest-worker \
		--name pyspark-pytest-worker \
		--volume $(PATH_REPOSITORY)/examples:/tmp/examples \
		--workdir /tmp/examples \
		$(IMAGE) \
		/bin/bash

docker-exec-worker:
	docker exec -it \
		pyspark-pytest-master \
		/bin/bash
