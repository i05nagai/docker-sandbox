PATH_TO_THIS_DIR := $(dir $(realpath $(lastword ${MAKEFILE_LIST})))
PATH_TO_PARENT_DIR := $(dir $(realpath $(PATH_TO_THIS_DIR)))
include ../../script/make/build_docker_image.mk
DOCKER_BUILD_PATH = ..
DOCKER_DOCKERFILE_PATH := Dockerfile

docker-run-collector:
	docker run \
		-p 127.0.0.1:4317:4317 \
		-p 127.0.0.1:4318:4318 \
		-p 127.0.0.1:55679:55679 \
		--name collector \
		$(IMAGE) \
		2>&1 | tee collector-output.txt # Optionally tee output for easier search later

docker-run:
	docker run \
		-p 127.0.0.1:4317:4317 \
		-p 127.0.0.1:4318:4318 \
		-p 127.0.0.1:55679:55679 \
		--name collector \
		$(IMAGE) \
		2>&1 | tee collector-output.txt # Optionally tee output for easier search later
