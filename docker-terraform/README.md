## Overview
Docker image for terraform linter and formatter.

* terraform
* make

## Lint

```
docker run --rm -it \
    i05nagai/terraform:latest \
    lint <path-to-terraform-dir>
```

## Formatter

```
docker run --rm -it \
    i05nagai/terraform:latest \
    fmt <path-to-terraform-dir>
```
