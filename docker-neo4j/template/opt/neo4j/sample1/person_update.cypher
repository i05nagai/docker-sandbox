MATCH (p:Person {name: "Alice"})
SET p.age = 35;
MATCH (n:Person {name: "Bob"})
SET n += {age: 40, city: "Tokyo"};
