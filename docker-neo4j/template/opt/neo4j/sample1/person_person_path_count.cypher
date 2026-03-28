MATCH path = (a:Person {name: "Alice"})-[*]-(b:Person {name: "Bob"})
RETURN a, count(path) AS numberOfPaths;
