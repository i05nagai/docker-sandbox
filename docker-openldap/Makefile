include ../script/make/build_directory.mk

docker-run:
	docker run --rm -it \
		--name openldap \
		-p 8888:80 \
		${IMAGE} /bin/bash
