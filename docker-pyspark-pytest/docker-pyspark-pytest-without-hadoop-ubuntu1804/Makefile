NAME = pyspark-pytest-without-hadoop-ubuntu1804
include ../../script/make/build_docker_image.mk

DOCKER_DOCKERFILE_PATH = Dockerfile
DOCKER_BUILD_PATH = ..

docker-run:
	docker run --rm -it \
		--name pyspark-pytest-without-hadoop \
		--volume $(shell cd .. && pwd)/examples:/tmp/examples \
		--workdir /tmp/examples \
		$(IMAGE) \
		/bin/bash
