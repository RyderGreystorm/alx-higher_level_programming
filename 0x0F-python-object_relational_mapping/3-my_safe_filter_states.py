#!/usr/bin/python3
"""Preventing SQL Injection"""


import sys
import MySQLdb


def run():
    """COde definition"""

    u_name = sys.argv[1]
    pswd = sys.argv[2]
    db_name = sys.argv[3]
    s_query = sys.argv[4]

    db = MySQLdb.connect(
            host='localhost',
            user=u_name,
            passwd=pswd,
            db=db_name)

    cursor = db.cursor()
    query = """
            SELECT *
            FROM states
            WHERE BINARY states.name LIKE %s
            ORDER BY states.id
            """

    cursor.execute(query, (s_query + '%',))
    result = cursor.fetchall()

    for row in result:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    run()
