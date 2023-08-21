#!/usr/bin/python3
"""Listing all cities from the database"""


import sys
import MySQLdb


def run():
    """snippet to find cities"""

    uname = sys.argv[1]
    pswd = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
            host='localhost',
            user=uname,
            passwd=pswd,
            db=db_name)

    cursor = db.cursor()
    query = """
            SELECT cities.id,cities.name, states.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            ORDER BY cities.id
            """
    cursor.execute(query)
    result = cursor.fetchall()

    for row in result:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    run()
