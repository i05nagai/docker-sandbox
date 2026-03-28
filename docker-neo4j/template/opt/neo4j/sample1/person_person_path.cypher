MATCH (a:Person {name: "Alice"}), (b:Person {name: "Bob"})
RETURN a, EXISTS((a)-[*]-(b)) AS pathExists;
