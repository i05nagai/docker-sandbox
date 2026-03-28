MATCH (a:Person {name: 'Alice'}), (b:Address {name: 'address1'})
CREATE (a)-[:BELONG {moved_at: 2020}]->(b);
