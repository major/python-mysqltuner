#!/usr/bin/env python
import psutil
import pymysql
from pprint import pprint


from . import mysqltuner


def run_mysqltuner():

  m = mysqltuner.MysqlTuner()

  # db_creds = {
  #   'host': 'localhost',
  #   'user': 'root',
  # }

  # conn = pymysql.connect(**db_creds)

  # cur = conn.cursor()

  # queries = [
  #   "SHOW /*!50000 GLOBAL */ VARIABLES",
  #   "SHOW /*!50000 GLOBAL */ STATUS"
  # ]

  # for query in queries:
  #   cur.execute(query)

  #   for row in cur:
  #     print(row)


  # cur.close()
  # conn.close()

  # pprint(psutil.virtual_memory())
  # pprint(psutil.swap_memory())
