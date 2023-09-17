#!/usr/bin/python3
"""
get all states
"""
import MySQLdb
from sys import argv


if __name__ == '__main__':
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        database=argv[3]
    )

    mycursor = db.cursor()
    s = "SELECT cities.name FROM cities, states\
    	WHERE cities.state_id = states.id AND states.name = %s\
        ORDER BY cities.id"
    d = (argv[4],)
    mycursor.execute(s, d)

    rows = mycursor.fetchall()
    q = ', '.join([row[0] for row in rows])
    print(q)
