DOCKER_IMAGE_PREFIX = i05nagai/
DOCKER_COMMAND = gcloud docker --
DIRNAME = $(shell basename $(shell pwd))
NAME = $(subst docker-,,${DIRNAME})
VERSION ?= latest
IMAGE = ${DOCKER_IMAGE_PREFIX}${NAME}
DOCKER_BUILD_ARGS = --build-arg DOCKER_IMAGE_PREFIX=${DOCKER_IMAGE_PREFIX}

build: pre-build docker-build post-build

pre-build:

post-build:

docker-build:
	docker build -t ${IMAGE}:${VERSION} ${DOCKER_BUILD_ARGS} .

push: docker-push post-push

post-push:

docker-push:
	${DOCKER_COMMAND} push ${IMAGE}:${VERSION}
