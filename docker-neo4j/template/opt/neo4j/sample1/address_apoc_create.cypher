CALL apoc.trigger.add(
  'auto-uuid-persons-only',
  'UNWIND $createdNodes AS n
   WHERE "Person" IN labels(n)
   SET n.uuid = apoc.create.uuid()',
  {phase:'after'}
)
