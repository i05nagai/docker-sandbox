MATCH path = (a:Person {name: "Alice"})-[*1..3]-(b)
RETURN path;
