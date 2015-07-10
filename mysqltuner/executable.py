#!/usr/bin/env python
import click
import psutil
import pymysql
from pprint import pprint


from . import mysqltuner


@click.command()
def run_mysqltuner():
  click.echo("Running MySQLTuner")
