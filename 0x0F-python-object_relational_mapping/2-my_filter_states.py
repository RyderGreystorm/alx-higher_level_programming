#!/usr/bin/python3
"""Taking Search params from user"""


import sys
import MySQLdb


def run():
    """Uses arguments on cmd_line"""

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

    query = r"SELECT * FROM states WHERE name = '{}'".format(s_query)
    cursor.execute(query)
    result = cursor.fetchall()

    for row in result:
        print(row)


if __name__ == "__main__":
    run()
