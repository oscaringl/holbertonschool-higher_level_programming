-- lists all records with a score >= 10 of the database
SELECT score, name FROM second_table
WHERE score >= 10
ORDER BY score DESC, name ASC;
