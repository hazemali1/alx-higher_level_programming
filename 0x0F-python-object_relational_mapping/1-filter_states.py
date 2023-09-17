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
    s = "SELECT * FROM states WHERE name LIKE %s ORDER BY states.id"
    d = ('N%',)
    mycursor.execute(s, d)

    for row in mycursor.fetchall():
        print(row)
