#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa,
but safe from sql attacks """
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    query = """SELECT cities.id, cities.name,
    states.name FROM cities INNER JOIN states ON states.id=cities.state_id"""
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
