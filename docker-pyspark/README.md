## Overview
Docker image for PySpark.
There are two images 

* (a) base image is Alpine Linux
    * (a-1) without spark history server
    * (a-2) with spark history server
* (b) base image is Ubuntu

## (a) alpine based
This Docker image helps you to run Spark (on Docker) with the following installed:

1. [Apache Spark](https://spark.apache.org/) 2.1.1
    * running on Hadoop 2.7.3 and Java openjdk version "1.8.0_92-internal"
2. Python 3.4.3
3. Spark's python interface
    * [Welcome to Spark Python API Docs! — PySpark 2.1.1 documentation](http://spark.apache.org/docs/latest/api/python/index.html)


### Building docker images
(a-1) without spark history server

```
make alpine
```

(a-2) with spark history server

```
make alpine-spark-history-server
```

### Starting pyspark

```
docker pull i05nagai/pyspark-alpine:latest
docker run --rm -it i05nagai/pyspark-alpine:latest /bin/bash
$ ./bin/pyspark
```

### docker-compose.yml example files

```
cd example
docker-compose up  # launch cluster (Ctrl-C to stop)
```

The SparkUI will be running at `http://${YOUR_DOCKER_HOST}:8080` with one
worker listed. To run `pyspark`, exec into a container:

```
docker exec -it example_master_1 /bin/bash
bin/pyspark
```

## (b) ubuntu based

### Building the docker image

```
make alpine
make alpine-spkar-history-servrer
make alpine-spkar-history-servrer
```

## Troubleshooting
If you are unable to access HDFS from pyspark, try running pyspark with the `--master yarn` flag.

If you are unable to access the HTTP SparkUI, verify that the open ports are redirected from your virtual machine to your host machine. Under VirtualBox, see the machine's `Settings > Network > Port Forwarding`.

## Reference


## Updating Docker images

If you change the version of pytest, you need to add git-tag to the commit.
For instance, if the version of Hadoop is `2.7.3` and version of Spark is `2.1.2`, you need to execute the following commands.

```
git tag -a spark-2.1.2-hadoop-2.7.3
git push origin spark-2.1.2-hadoop-2.7.3
```
