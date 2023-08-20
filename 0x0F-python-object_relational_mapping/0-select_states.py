#!/usr/bin/python3
"""Passing queries to mysql server using MySQLdb"""


import sys
import MySQLdb


def run():
    """MySQLdb"""

    my_username = sys.argv[1]
    my_pwd = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=my_username,
            passwd=my_pwd,
            db=db_name)

    cursor = db.cursor()
    query = r'SELECT * FROM states ORDER BY states.id LIMIT 5'
    cursor.execute(query)

    results = cursor.fetchall()

    # Display results
    for row in results:
        print(row)

    cursor.close()


if __name__ == "__main__":
    run()
