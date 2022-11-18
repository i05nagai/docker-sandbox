

## Install
- [Apache Flink 1\.10 Documentation: Local Setup Tutorial](https://ci.apache.org/projects/flink/flink-docs-stable/getting-started/tutorials/local_setup.html)

## Usage
Run Flink

```
make docker-run
$FLINK_HOME/bin/start-cluster.sh
```

project1

```
cd project1
gradle build
$FLINK_HOME/bin/flink run -c project1.App build/libs/project1-0.1.0.BUILD-SNAPSHOT.jar
```

project5

```
cd project5
sbt package
$FLINK_HOME/bin/flink run -c org.example.WordCount target/scala-2.11/project5_2.11-0.1-SNAPSHOT.jar
```

`http://localhost:8081/#/overview`


```
mvn archetype:generate \
    -DarchetypeGroupId=org.apache.flink \
    -DarchetypeArtifactId=flink-walkthrough-datastream-java \
    -DarchetypeVersion=1.11-SNAPSHOT \
    -DgroupId=frauddetection \
    -DartifactId=frauddetection \
    -Dversion=0.1 \
    -Dpackage=spendreport \
    -DinteractiveMode=false
```

## Scala
https://nightlies.apache.org/flink/flink-docs-release-1.3/quickstart/scala_api_quickstart.html
Create a new project in Scala.

```
sbt new tillrohrmann/flink-project.g8
```

## metrics
https://nightlies.apache.org/flink/flink-docs-master/docs/deployment/metric_reporters/

## Reference
- [Apache Flink 1\.10 Documentation: Flink Operations Playground](https://ci.apache.org/projects/flink/flink-docs-release-1.10/getting-started/docker-playgrounds/flink-operations-playground.html)
- [apache/flink\-playgrounds: Apache Flink Playgrounds](https://github.com/apache/flink-playgrounds)
- [apache/flink\-docker: Docker packaging for Apache Flink](https://github.com/apache/flink-docker)
- [dataArtisans/infoworld\-post: Code examples for a blog post on infoworld\.com](https://github.com/dataArtisans/infoworld-post)
