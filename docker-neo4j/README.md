

```
Directories in use:
home:         /var/lib/neo4j
config:       /etc/neo4j
logs:         /var/log/neo4j
plugins:      /var/lib/neo4j/plugins
import:       /var/lib/neo4j/import
data:         /var/lib/neo4j/data
certificates: /var/lib/neo4j/certificates
licenses:     /var/lib/neo4j/licenses
run:          /var/lib/neo4j/run
```

```
cypher-shell
```


# DBMS
https://neo4j.com/docs/operations-manual/current/database-administration/syntax/


```
SHOW DATABSES;
show relationship 
```

- 'FOREACH'
- 'ALTER'
- 'ORDER BY'
- 'CALL'
- 'USING PERIODIC COMMIT'
- 'CREATE'
- 'LOAD CSV'
- 'START DATABASE'
- 'STOP DATABASE'
- 'DEALLOCATE'
- 'DELETE'
- 'DENY'
- 'DETACH'
- 'DROP'
- 'DRYRUN'
- 'FINISH'
- 'GRANT'
- 'INSERT'
- 'LIMIT'
- 'MATCH'
- 'MERGE'
- 'NODETACH'
- 'OFFSET'
- 'OPTIONAL'
- 'REALLOCATE'
- 'REMOVE'
- 'RENAME'
- 'RETURN'
- 'REVOKE'
- 'ENABLE SERVER'
- 'SET'
- 'SHOW'
- 'SKIP'
- 'TERMINATE'
- 'UNWIND'
- 'USE'
- 'WITH'


# apoc
https://neo4j.com/labs/apoc/


https://neo4j.com/labs/apoc/4.4/background-operations/triggers/

In neo4j.conf

```
#dbms.security.procedures.allowlist=apoc.coll.*,apoc.load.*,gds.*
dbms.security.procedures.allowlist=apoc.trigger.*
```

## Reference
- https://github.com/neo4j/docker-neo4j
