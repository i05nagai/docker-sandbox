#!/bin/bash

cypher-shell -a neo4j://localhost:7687
cypher-shell -a neo4j://localhost:7474

neo4j-admin dbms set-initial-password 11111111
neo4j start
