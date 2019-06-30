
## Concepts
- Index
    - database in RDB
- Type
    - table in RDB
- Document
    - record in RDB

## Commands

- `<type>`
    - `_doc`


Creating document

```
PUT /<index>/<type>/<id>
POST /<index>/<type>/
```

```
GET /<index>/<type>/<id>
```

Partially update

```
POST /<index>/_update/<document-id>
```

Delete document

```
DELETE /<index>/_doc/<id>
```

Delete index

```
DELETE /<index>
```

Access

```
POST /<index>/<type>/_bulk
{"index": {"_id": 1}}
{"title": "1", "price": 1}
```

```
GET /<index>/<type>/_search?size=3
{
  "query": {
    "match": {
      "title": "quick dog"
    }
  }
}
```

## Running elasticsearch
- [Starting Elasticsearch \| Elasticsearch Reference \[7\.2\] \| Elastic](https://www.elastic.co/guide/en/elasticsearch/reference/current/starting-elasticsearch.html)

## Directory strcture

- `elasticsearch.yml`
    - for configuring Elasticsearch
- `jvm.options`
    - for configuring Elasticsearch JVM settings
- `log4j2.properties`
    - for configuring Elasticsearch logging


## Configuration
- [Configuring Elasticsearch \| Elasticsearch Reference \[7\.2\] \| Elastic](https://www.elastic.co/guide/en/elasticsearch/reference/current/settings.html)
- [Bootstrapping a cluster \| Elasticsearch Reference \[master\] \| Elastic](https://www.elastic.co/guide/en/elasticsearch/reference/master/modules-discovery-bootstrap-cluster.html)


## Reference
- [Install Elasticsearch with Debian Package \| Elasticsearch Reference \[7\.2\] \| Elastic](https://www.elastic.co/guide/en/elasticsearch/reference/current/deb.html)
