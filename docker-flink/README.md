

## Install
- [Apache Flink 1\.10 Documentation: Local Setup Tutorial](https://ci.apache.org/projects/flink/flink-docs-stable/getting-started/tutorials/local_setup.html)


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


## Reference
- [Apache Flink 1\.10 Documentation: Flink Operations Playground](https://ci.apache.org/projects/flink/flink-docs-release-1.10/getting-started/docker-playgrounds/flink-operations-playground.html)
- [apache/flink\-playgrounds: Apache Flink Playgrounds](https://github.com/apache/flink-playgrounds)
- [apache/flink\-docker: Docker packaging for Apache Flink](https://github.com/apache/flink-docker)
- [dataArtisans/infoworld\-post: Code examples for a blog post on infoworld\.com](https://github.com/dataArtisans/infoworld-post)
