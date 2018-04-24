## Overview


```
/monitor
--source=heapster:http://localhost:8082?whitelisted=stackdriver_requests_count,stackdriver_timeseries_count
--stackdriver-prefix=container.googleapis.com/internal/addons
--api-override=https://monitoring.googleapis.com/
--pod-id=$(POD_NAME)
--namespace-id=$(POD_NAMESPACE)
```

## Reference
