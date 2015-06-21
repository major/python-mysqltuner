#!/usr/bin/env python
from easydict import EasyDict
import psutil
import pymysql
import termcolor
import time


class MysqlTuner(object):

  def __init__(self):
    self.data = EasyDict()
    self.get_system_data()
    print(self.data)


  def get_system_data(self):

    def get_ram():
      return psutil.virtual_memory().total

    def get_swap():
      return psutil.swap_memory().total

    def get_uptime():
      return int(time.time())-psutil.boot_time()

    self.data.ram = get_ram()
    self.data.swap = get_swap()
    self.data.uptime = get_uptime()