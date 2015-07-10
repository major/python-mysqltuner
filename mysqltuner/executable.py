#!/usr/bin/env python
import click


# from . import mysqltuner


@click.command()
def run_mysqltuner():
    click.echo("Running MySQLTuner")
