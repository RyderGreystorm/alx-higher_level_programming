#!/usr/bin/python3
"""Filtering data tp return data matching  wildcard"""


import sys
import MySQLdb


def run():
    """Code definition"""

    user = sys.argv[1]
    pswd = sys.argv[2]
    db_name = sys.argv[3]

    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            passwd=pswd,
            db=db_name)

    cursor = db.cursor()
    query = r"SELECT * FROM states WHERE name  LIKE 'N%' ORDER BY states.id"

    cursor.execute(query)
    result = cursor.fetchall()

    for row in result:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    run()
