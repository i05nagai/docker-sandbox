## Ubuntu based
This Docker image helps you to run Spark (on Docker) with the following installed:

1. [Apache Spark](https://spark.apache.org/) 2.1.1
    * running on Hadoop 2.7.3 and Java openjdk version "1.8.0_92-internal"
2. Python 3.4.8
3. Spark's python interface
    * [Welcome to Spark Python API Docs! — PySpark 2.1.1 documentation](http://spark.apache.org/docs/latest/api/python/index.html)

### Building the docker image

```
make
```

### Starting pyspark history server
See [Monitoring and Instrumentation - Spark 2.2.0 Documentation](https://spark.apache.org/docs/2.2.0/monitoring.html).

```
docker pull i05nagai/pyspark-alpine-spark-history-server:latest
```

You need to put your logs into `alpine-spark-history-server/logs` then execute 

```
docker run --rm \
  -p 18080:18080 \
  --name pyspark \
  --volume $(pwd)/logs:/opt/local/pyspark/logs \
  i05nagai/pyspark-alpine-spark-history-server \
  /bin/bash /opt/local/pyspark/run_spark_history_server.sh
```

See `docker_run.sh` for details.

## Troubleshooting
If you are unable to access HDFS from pyspark, try running pyspark with the `--master yarn` flag.

If you are unable to access the HTTP SparkUI, verify that the open ports are redirected from your virtual machine to your host machine. Under VirtualBox, see the machine's `Settings > Network > Port Forwarding`.

## Reference
