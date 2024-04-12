#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa,
but safe from sql attacks """
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("""
        SELECT
            cities.id, cities.name
        FROM
            cities
        JOIN
            states
        ON
            cities.state_id = states.id
        WHERE
            states.name LIKE BINARY %s
        ORDER BY
            cities.id ASC
    """, (sys.argv[4],))
    rows_selected = cur.fetchall()

    if rows_selected is not None:
        print(", ".join([row[1] for row in rows_selected]))

    cur.close()
    db.close()
