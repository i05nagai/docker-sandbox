
DOCKER_BUILD_PATH = ../
include ../../script/make/build_docker_image.mk

TEMPALTE_PATH = $(shell cd .. && pwd)

run:
	$(DOCKER) run \
		--rm \
		--workdir /template/opt/fluent-bit \
		-v $(TEMPALTE_PATH)/template:/template \
		--name fluent-bit \
		-it \
		$(IMAGE) /bin/bash

attach:
	$(DOCKER) exec \
		-w /var/log \
		-it \
		fluent-bit /bin/bash
