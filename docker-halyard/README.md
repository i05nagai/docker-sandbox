
## Overview

```
docker run -p 8084:8084 -p 9000:9000 \
    --name halyard --rm \
    -v ~/.hal:/home/spinnaker/.hal \
    -it \
    gcr.io/spinnaker-marketplace/halyard:stable
```

## Reference
https://www.spinnaker.io/setup/install/halyard/
