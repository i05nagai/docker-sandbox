

```
export FLINK_PROPERTIES="jobmanager.rpc.address: jobmanager"
make docker-network-create
make docker-jobmanager
make docker-taskmanager
make docker-network-rm
```


https://github.com/apache/flink-docker/blob/master/
