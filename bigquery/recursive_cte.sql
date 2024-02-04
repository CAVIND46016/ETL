WITH RECURSIVE unnested_tmp AS
  (SELECT 'x1' AS package_id,
          'x2' AS child_id
   UNION ALL SELECT 'x1',
                    'x3'
   UNION ALL SELECT 'x1',
                    'x4'
   UNION ALL SELECT 'x1',
                    'x5'
   UNION ALL SELECT 'x6',
                    'x1'
   UNION ALL SELECT 'x6',
                    'x9'),
               iterations AS
  (SELECT package_id,
          child_id
   FROM unnested_tmp
   UNION ALL SELECT b.package_id,
                    a.child_id
   FROM unnested_tmp a
   JOIN iterations b ON b.child_id = a.package_id)
SELECT DISTINCT *
FROM iterations
ORDER BY package_id,
         child_id


-- OUTPUT:
-- +--------------+------------+
-- | package_id   | child_id   |
-- |--------------+------------|
-- | x1           | x2         |
-- | x1           | x3         |
-- | x1           | x4         |
-- | x1           | x5         |
-- | x6           | x1         |
-- | x6           | x2         |
-- | x6           | x3         |
-- | x6           | x4         |
-- | x6           | x5         |
-- | x6           | x9         |
-- +--------------+------------+
