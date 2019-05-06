

```
make docker-network
make docker-run-kafka-zookeeper
make docker-run-kafka-keeper
```


```
kafka-console-consumer.sh <option>
```

* `--bootstrap-server <String: server to connect to>`
    * REQUIRED: The server(s) to connect to.
* `--consumer-property <String: consumer_prop>`
    * A mechanism to pass user-defined properties in the form key=value to the consumer.
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
* `--key-deserializer <String: deserializer for key>`
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
* `--value-deserializer <String: deserializer for values>`
* `--whitelist <String: whitelist>` 
    * Whitelist of topics to include for consumption.

## TLS configuration for kafka server
- [Security Tutorial — Confluent Platform](https://docs.confluent.io/current/tutorials/security_tutorial.html#generating-keys-certs)
- [Apache Kafka](https://kafka.apache.org/documentation/#security)

```
# Without user prompts, pass command line arguments
$ keytool \
    -genkey \
    -keystore credential/kafka.server.keystore.jks \
    -alias kafka-server \
    -validity 3650 \
    -storepass serverkeystore \
    -keyalg RSA \
    -ext SAN=DNS:kafka-server \
    -keypass serverkeystore

#     -dname kafka-server \
#     -ext SAN=DNS:kafka-server
# With user prompts
# you need a password for keystore and a password for key
$ keytool \
    -keystore kafka.server.keystore.jks \
    -alias kafka-server \
    -validity 3650 \
    -genkey \
    -keyalg RSA \
    -ext SAN=DNS:kafka-server \
Enter keystore password:
Re-enter new password:
What is your first and last name?
  [Unknown]:  i05nagai
What is the name of your organizational unit?
  [Unknown]:  organization
What is the name of your organization?
  [Unknown]:  organization_name
What is the name of your City or Locality?
  [Unknown]:
What is the name of your State or Province?
  [Unknown]:
What is the two-letter country code for this unit?
  [Unknown]:
Is CN=i05nagai, OU=organization, O=organization_name, L=Unknown, ST=Unknown, C=Unknown correct?
  [no]:  yes

Enter key password for <kafka-server>
        (RETURN if same as keystore password):
Re-enter new password:
```

Verify the generated key

```
# you need password for keystore
$ keytool -list -v -keystore credential/kafka.server.keystore.jks
Enter keystore password:
Keystore type: jks
Keystore provider: SUN

Your keystore contains 1 entry

Alias name: kafka-server
Creation date: May 4, 2019
Entry type: PrivateKeyEntry
Certificate chain length: 1
Certificate[1]:
Owner: CN=i05nagai, OU=organization, O=organization_name, L=Unknown, ST=Unknown, C=Unknown
Issuer: CN=i05nagai, OU=organization, O=organization_name, L=Unknown, ST=Unknown, C=Unknown
Serial number: 2d235a7d
Valid from: Sat May 04 19:26:54 GMT 2019 until: Tue Apr 16 19:26:54 GMT 2030
Certificate fingerprints:
         MD5:  B3:25:55:AD:66:68:37:BD:D8:6D:63:4D:DB:6B:DE:38
         SHA1: 06:9C:67:7E:EF:09:02:7C:A3:8F:F8:9A:A5:DB:44:21:FE:07:82:4E
         SHA256: 78:DB:74:35:9B:AE:9D:51:2E:39:3D:37:A8:3B:8C:90:D5:C6:18:D0:CD:56:7E:90:BA:D2:5B:9D:D2:A2:23:FD
Signature algorithm name: SHA256withRSA
Subject Public Key Algorithm: 2048-bit RSA key
Version: 3

Extensions:

#1: ObjectId: 2.5.29.17 Criticality=false
SubjectAlternativeName [
  DNSName: kafka-server
]

#2: ObjectId: 2.5.29.14 Criticality=false
SubjectKeyIdentifier [
KeyIdentifier [
0000: 81 55 9F B2 88 62 39 E3   59 20 00 B3 2A A8 0C C3  .U...b9.Y ..*...
0010: 8C 68 A3 94                                        .h..
]
]
```

Generate a CA that is simply a public-private key pair and certificate, and it is intended to sign other certificates.

```
# This creates kafka-server.key and kafka-server.ca-cert
# you need a password for PEM (kafka-server.ca-key)
# password: ca-keykafka-server
$ openssl req \
    -new \
    -x509 \
    -keyout credential/kafka-server.ca-key \
    -out credential/kafka-server.ca-cert \
    -days 3650
writing new private key to 'ca-key'
Enter PEM pass phrase:
Verifying - Enter PEM pass phrase:
-----
You are about to be asked to enter information that will be incorporated
into your certificate request.
What you are about to enter is what is called a Distinguished Name or a DN.
There are quite a few fields but you can leave some blank
For some fields there will be a default value,
If you enter '.', the field will be left blank.
-----
Country Name (2 letter code) [AU]:
State or Province Name (full name) [Some-State]:
Locality Name (eg, city) []:
Organization Name (eg, company) [Internet Widgits Pty Ltd]:
Organizational Unit Name (eg, section) []:
Common Name (e.g. server FQDN or YOUR name) []:kafka-server
Email Address []:
```

Add the generated CA to the clients’ truststore so that the clients can trust this CA:

```
keytool \
    -keystore credential/kafka.client.truststore.jks \
    -alias CARoot \
    -storepass clienttruststore \
    -import -file credential/kafka-server.ca-cert
```

Add the generated CA to the brokers' truststore so that the brokers can trust this CA.

```
keytool \
    -keystore credential/kafka.server.truststore.jks \
    -alias CARoot \
    -storepass servertruststore \
    -importcert -file credential/kafka-server.ca-cert
```

Export the certificate from the keystore:

```
keytool \
    -keystore credential/kafka.server.keystore.jks \
    -alias kafka-server \
    -storepass serverkeystore \
    -certreq -file credential/kafka-server.cert-file
```

Sign it with the CA:

```
# pass is password for kafka-server.ca-key
openssl x509 \
    -req \
    -CA credential/kafka-server.ca-cert \
    -CAkey credential/kafka-server.ca-key \
    -in credential/kafka-server.cert-file \
    -out credential/kafka-server.cert-signed \
    -days 3650 \
    -CAcreateserial \
    -passin pass:ca-keykafka-server
```

Import both the certificate of the CA and the signed certificate into the broker keystore:

```
keytool \
    -keystore credential/kafka.server.keystore.jks \
    -alias CARoot \
    -storepass serverkeystore \
    -import -file credential/kafka-server.ca-cert
```

```
keytool \
    -keystore credential/kafka.server.keystore.jks \
    -alias kafka-server \
    -storepass serverkeystore \
    -import -file credential/kafka-server.cert-signed
```

Check TLS connection

```
openssl s_client -debug -connect kafka-server:9093 -tls1
```

## TLS configuration for kafka client

```
keytool \
    -keystore credential/kafka.client.keystore.jks \
    -alias kafka-server \
    -storepass clientkeystore \
    -import \
    -file credential/kafka-server.cert-signed
```

```
keytool \
    -keystore credential/kafka.client.keystore.jks \
    -alias kafka-server \
    -validity 3650 \
    -genkey \
    -storepass clientkeystore \
    -keyalg RSA
```

## Configuration
- Consumer
    - [Apache Kafka](http://kafka.apache.org/documentation.html#consumerconfigs)

## Reference
- [Running Kafka in Production — Confluent Platform](https://docs.confluent.io/current/kafka/deployment.html)
- [Apache Kafka](https://kafka.apache.org/downloads)
- [Structured Streaming \+ Kafka Integration Guide \(Kafka broker version 0\.10\.0 or higher\) \- Spark 2\.2\.0 Documentation](https://spark.apache.org/docs/2.2.0/structured-streaming-kafka-integration.html)
