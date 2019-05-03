

```
make docker-network
make docker-run-kafka-zookeeper
make docker-run-kafka-keeper
```


```
kafka-console-consumer.sh 
--bootstrap-server <String: server to    REQUIRED: The server(s) to connect to.
  connect to>
--consumer-property <String:             A mechanism to pass user-defined
  consumer_prop>                           properties in the form key=value to
                                           the consumer.
--consumer.config <String: config file>  Consumer config properties file. Note
                                           that [consumer-property] takes
                                           precedence over this config.
--enable-systest-events                  Log lifecycle events of the consumer
                                           in addition to logging consumed
                                           messages. (This is specific for
                                           system tests.)
--formatter <String: class>              The name of a class to use for
                                           formatting kafka messages for
                                           display. (default: kafka.tools.
                                           DefaultMessageFormatter)
--from-beginning                         If the consumer does not already have
                                           an established offset to consume
                                           from, start with the earliest
                                           message present in the log rather
                                           than the latest message.
--group <String: consumer group id>      The consumer group id of the consumer.
--isolation-level <String>               Set to read_committed in order to
                                           filter out transactional messages
                                           which are not committed. Set to
                                           read_uncommittedto read all
                                           messages. (default: read_uncommitted)
--key-deserializer <String:
  deserializer for key>
--max-messages <Integer: num_messages>   The maximum number of messages to
                                           consume before exiting. If not set,
                                           consumption is continual.
--offset <String: consume offset>        The offset id to consume from (a non-
                                           negative number), or 'earliest'
                                           which means from beginning, or
                                           'latest' which means from end
                                           (default: latest)
--partition <Integer: partition>         The partition to consume from.
                                           Consumption starts from the end of
                                           the partition unless '--offset' is
                                           specified.
--property <String: prop>                The properties to initialize the
                                           message formatter. Default
                                           properties include:
                                                print.timestamp=true|false
                                                print.key=true|false
                                                print.value=true|false
                                                key.separator=<key.separator>
                                                line.separator=<line.separator>
                                                key.deserializer=<key.deserializer>
                                                value.deserializer=<value.
                                           deserializer>
                                         Users can also pass in customized
                                           properties for their formatter; more
                                           specifically, users can pass in
                                           properties keyed with 'key.
                                           deserializer.' and 'value.
                                           deserializer.' prefixes to configure
                                           their deserializers.
--skip-message-on-error                  If there is an error when processing a
                                           message, skip it instead of halt.
--timeout-ms <Integer: timeout_ms>       If specified, exit if no message is
                                           available for consumption for the
                                           specified interval.
--topic <String: topic>                  The topic id to consume on.
--value-deserializer <String:
  deserializer for values>
--whitelist <String: whitelist>          Whitelist of topics to include for
                                           consumption.
```

## Configuration
- Consumer
    - [Apache Kafka](http://kafka.apache.org/documentation.html#consumerconfigs)

## Reference
- [Running Kafka in Production — Confluent Platform](https://docs.confluent.io/current/kafka/deployment.html)
- [Apache Kafka](https://kafka.apache.org/downloads)
- [Structured Streaming \+ Kafka Integration Guide \(Kafka broker version 0\.10\.0 or higher\) \- Spark 2\.2\.0 Documentation](https://spark.apache.org/docs/2.2.0/structured-streaming-kafka-integration.html)
