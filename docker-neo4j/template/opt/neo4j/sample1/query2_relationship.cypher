MATCH (a:Person)-[r:KNOWS]->(b:Person)
RETURN a.name, r.since, b.name;
