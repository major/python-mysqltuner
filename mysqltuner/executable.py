#!/usr/bin/env python
import pymysql


def run_mysqltuner():

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
