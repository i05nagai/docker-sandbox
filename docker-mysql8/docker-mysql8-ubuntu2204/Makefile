include ../../script/make/build_docker_image.mk

DOCKER_BUILD_PATH = ..

docker-run:
	$(DOCKER) \
		run \
		--rm \
		 -it \
		--env MYSQL_ROOT_PASSWORD \
		-p 3306:3306 \
		$(IMAGE) \
		/bin/bash

docker-mysql-server:
	$(DOCKER) \
		run \
		--rm \
		-it \
		-e MYSQL_ROOT_PASSWORD \
		-p 3306:3306 \
		$(IMAGE) \
		mysqld -D
