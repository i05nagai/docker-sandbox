PATH_TO_THIS_DIR := $(dir $(realpath $(lastword ${MAKEFILE_LIST})))
PATH_TO_PARENT_DIR := $(dir $(realpath $(PATH_TO_THIS_DIR)))
include ../../script/make/build_docker_image.mk
DOCKER_BUILD_PATH = ..
DOCKER_DOCKERFILE_PATH := Dockerfile

docker-run:
	docker run \
		--rm -it \
		-p 8080:8080 \
		-p 50000:50000 \
		--name jenkins \
		--volume /var/run/docker.sock:/var/run/docker.sock \
		--privileged \
		--volume ${PATH_TO_PARENT_DIR}/samples:/tmp/samples \
		--volume ${PATH_TO_PARENT_DIR}/jenkins_home:/var/jenkins_home \
		${IMAGE}
