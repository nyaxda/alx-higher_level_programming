-- lists all cities contained in the database hbtn_0d_usa.
SELECT id, name, states
FROM cities
    NATURAL JOIN states
ORDER BY id ASC;