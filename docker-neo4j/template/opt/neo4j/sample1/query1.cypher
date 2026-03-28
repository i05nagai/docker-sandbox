MATCH (n)
RETURN LABELS(n) AS label, n.id, n.name, n.age, n.city;
