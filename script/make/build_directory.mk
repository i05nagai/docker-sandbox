DIRECTORIES ?= $(wildcard *)
IGNORE_FILES ?= Makefile

DIRECTORIES_FILTERED = $(filter-out ${IGNORE_FILES},${DIRECTORIES})
# delete docker- prefix from each directory name
TARGETS = $(foreach DIR,${DIRECTORIES_FILTERED},$(subst docker-,,${DIR}))

PUSH_TARGETS = $(addprefix push-,${TARGETS})
DO_BUILD_TARGETS = $(addprefix do-build-,${TARGETS})
PRE_BUILD_TARGETS = $(addprefix pre-build-,${TARGETS})
POST_BUILD_TARGETS = $(addprefix post-build-,${TARGETS})

.PHONY: build push ${TARGETS} ${PUSH_TARGETS}

build: ${TARGETS}

push: build ${PUSH_TARGETS}

${TARGETS}:
	$(MAKE) -C docker-$@ build

${PUSH_TARGETS}:
	$(MAKE) -C $(subst push-,,$@) push
