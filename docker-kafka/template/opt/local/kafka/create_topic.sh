#!/bin/bash

# --config <String: name=value>            A topic configuration override for the topic being created or altered.The
#                                            following is a list of valid configurations:
#                                                 cleanup.policy
#                                                 compression.type
#                                                 delete.retention.ms
#                                                 file.delete.delay.ms
#                                                 flush.messages
#                                                 flush.ms
#                                                 follower.replication.throttled.
#                                            replicas
#                                                 index.interval.bytes
#                                                 leader.replication.throttled.replicas
#                                                 max.message.bytes
#                                                 message.downconversion.enable
#                                                 message.format.version
#                                                 message.timestamp.difference.max.ms
#                                                 message.timestamp.type
#                                                 min.cleanable.dirty.ratio
#                                                 min.compaction.lag.ms
#                                                 min.insync.replicas
#                                                 preallocate
#                                                 retention.bytes
#                                                 retention.ms
#                                                 segment.bytes
#                                                 segment.index.bytes
#                                                 segment.jitter.ms
#                                                 segment.ms
#                                                 unclean.leader.election.enable
#                                          See the Kafka documentation for full
#                                            details on the topic configs.
# --create                                 Create a new topic.
# --delete                                 Delete a topic
# --delete-config <String: name>           A topic configuration override to be
#                                            removed for an existing topic (see
#                                            the list of configurations under the
#                                            --config option).
# --describe                               List details for the given topics.
# --disable-rack-aware                     Disable rack aware replica assignment
# --force                                  Suppress console prompts
# --help                                   Print usage information.
# --if-exists                              if set when altering or deleting
#                                            topics, the action will only execute
#                                            if the topic exists
# --if-not-exists                          if set when creating topics, the
#                                            action will only execute if the
#                                            topic does not already exist
# --list                                   List all available topics.
# --partitions <Integer: # of partitions>  The number of partitions for the topic
#                                            being created or altered (WARNING:
#                                            If partitions are increased for a
#                                            topic that has a key, the partition
#                                            logic or ordering of the messages
#                                            will be affected
# --replica-assignment <String:            A list of manual partition-to-broker
#   broker_id_for_part1_replica1 :           assignments for the topic being
#   broker_id_for_part1_replica2 ,           created or altered.
#   broker_id_for_part2_replica1 :
#   broker_id_for_part2_replica2 , ...>
# --replication-factor <Integer:           The replication factor for each
#   replication factor>                      partition in the topic being created.
# --topic <String: topic>                  The topic to be create, alter or
#                                            describe. Can also accept a regular
#                                            expression except for --create option
# --topics-with-overrides                  if set when describing topics, only
#                                            show topics that have overridden
#                                            configs
# --unavailable-partitions                 if set when describing topics, only
#                                            show partitions whose leader is not
#                                            available
# --under-replicated-partitions            if set when describing topics, only
#                                            show under replicated partitions
# --zookeeper <String: hosts>              REQUIRED: The connection string for
#                                            the zookeeper connection in the form
#                                            host:port. Multiple hosts can be
#                                            given to allow fail-over.

${KAFKA_HOME}/bin/kafka-topics.sh \
  --create \
  --zookeeper kafka-zookeeper:2181 \
  --replication-factor 1 \
  --partitions 1 \
  --topic test
