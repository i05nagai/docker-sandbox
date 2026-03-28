MATCH (p:Person {name: "Alice"})-[r]->(other)
RETURN p, r, other;
