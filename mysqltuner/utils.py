#!/usr/bin/env python
import psutil
import time


def get_ram():
  return psutil.virtual_memory().total

def get_swap():
  return psutil.swap_memory().total

def get_uptime():
  return int(time.time())-psutil.boot_time()
