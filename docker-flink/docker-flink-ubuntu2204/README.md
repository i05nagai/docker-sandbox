

Create network

```
make docker-network-create
```

```
export FLINK_PROPERTIES="jobmanager.rpc.address: jobmanager"
make docker-jobmanager
make docker-taskmanager
```

http://localhost:8081/#/overview


```
$FLINK_HOME/bin/flink run -c project1.App ./build/libs/project1-0.1.0.BUILD-SNAPSHOT.jar
```

remove network

```
make docker-network-rm
```


## Reference
- https://github.com/apache/flink-docker/blob/master/
