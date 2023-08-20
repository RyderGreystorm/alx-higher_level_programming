#!/usr/bin/python3

import sys
import MySQLdb

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
query = 'SELECT * FROM states ORDER BY id LIMIT 5'
cursor.execute(query)

results = cursor.fetchall()

# Display results
for row in results:
    print(row)

cursor.close()
db.close()
