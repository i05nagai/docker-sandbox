# docker-pyspark

This Docker image helps you to run Spark (on Docker) with the following
installed:

1. [Apache Spark](https://spark.apache.org/) 2.1.1
    * running on Hadoop 2.7.3 and Java openjdk version "1.8.0_92-internal"
2. Python 3.4.3
3. Spark's python interface
    * [Welcome to Spark Python API Docs! — PySpark 2.1.1 documentation](http://spark.apache.org/docs/latest/api/python/index.html)


If you change the version of pytest, you need to add git-tag to the commit.
For instance, if the version of Hadoop is `2.7.3` and version of Spark is `2.1.2`, you need to execute the following commands.

```
git tag -a spark-2.1.2-hadoop-2.7.3
git push origin spark-2.1.2-hadoop-2.7.3
```

# Starting pyspark

## On any OS


```
# Pull the docker image
docker pull makotonagai/docker-pyspark:latest
# Run the following command to start the container and get a bash prompt
docker run --rm -it makotonagai/docker-pyspark:latest /bin/bash
$ ./bin/pyspark
```

To quit the interpreter, hit `<Ctrl> + D`.

# How to run a cluster of containers with [Docker Compose](http://docs.docker.com/compose)

## docker-compose.yml example files

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

# Building the docker image yourself

```
docker build -t <name-of-docker-image> .
```

# Troubleshooting
If you are unable to access HDFS from pyspark, try running pyspark with the
`--master yarn` flag.

If you are unable to access the HTTP SparkUI, verify that the open ports are
redirected from your virtual machine to your host machine. Under VirtualBox,
see the machine's `Settings > Network > Port Forwarding`.
