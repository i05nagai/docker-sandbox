NAME = pyspark-pytest-centos7.5.1804
include ../../script/make/build_docker_image.mk

DOCKER_DOCKERFILE_PATH = Dockerfile
DOCKER_BUILD_PATH = ..

docker-run:
	docker run --rm -it \
		--name pyspark-pytest \
		--volume $(shell cd .. && pwd)/examples:/tmp/examples \
		--workdir /tmp/examples \
		$(IMAGE) \
		/bin/bash
