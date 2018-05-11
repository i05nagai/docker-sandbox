## alpine based
This Docker image helps you to run Spark (on Docker) with the following installed:

1. [Apache Spark](https://spark.apache.org/) 2.1.1
    * running on Hadoop 2.7.3 and Java openjdk version "1.8.0_92-internal"
2. Python 3.4.3
3. Spark's python interface
    * [Welcome to Spark Python API Docs! — PySpark 2.1.1 documentation](http://spark.apache.org/docs/latest/api/python/index.html)


### Building docker images
```
make
```

### Starting pyspark

```
docker pull i05nagai/pyspark-alpine:latest
docker run --rm -it i05nagai/pyspark-alpine:latest /bin/bash
$ ./bin/pyspark
```

## Troubleshooting
If you are unable to access HDFS from pyspark, try running pyspark with the `--master yarn` flag.

If you are unable to access the HTTP SparkUI, verify that the open ports are redirected from your virtual machine to your host machine. Under VirtualBox, see the machine's `Settings > Network > Port Forwarding`.

## Reference
