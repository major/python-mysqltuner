#!/usr/bin/env python
from datetime import datetime
import pymysql


d = datetime.now()
print(d.isoformat())

db_creds = {
  'host': 'localhost',
  'user': 'root',
}

conn = pymysql.connect(**db_creds)

cur = conn.cursor()

queries = [
  "SHOW /*!50000 GLOBAL */ VARIABLES",
  "SHOW /*!50000 GLOBAL */ STATUS"
]

for query in queries:
  cur.execute(query)

  for row in cur:
    print(row)


cur.close()
conn.close()
