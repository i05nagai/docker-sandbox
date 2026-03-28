MATCH (n: Person)
RETURN LABELS(n) AS label, n.personId;
