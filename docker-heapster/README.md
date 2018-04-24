## Overview

`kubernetes/heapster` is officitially provided docker imgae.

```
/heapster
--source=kubernetes.summary_api:''
--sink=stackdriver:?cluster_name=cluster-name&use_old_resources=true&use_new_resources=false&min_interval_sec=100&batch_export_timeout_sec=110
```

## Reference
[kubernetes/heapster: Compute Resource Usage Analysis and Monitoring of Container Clusters](https://github.com/kubernetes/heapster)
