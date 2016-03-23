#! /usr/bin/python

"""
database-check.py

This script will check whether the postgres container is up and running. It'll
connect to the database with the credentials provided in the environment
variables.
"""

import os
import sys
import MySQLdb


def database_check():
    dbname = os.environ.get('MYSQL_DATABASE')
    user = os.environ.get('MYSQL_USER')
    password = os.environ.get('MYSQL_PASSWORD')
    host = os.environ.get('MYSQL_HOST')
    port = int(os.environ.get('MYSQL_PORT'))

    print("HOST: {host}:{port}, DB: {dbname}, USER: {user}".format(
        dbname=dbname,
        user=user,
        host=host,
        port=port))

    try:
        MySQLdb.connect(
            db=dbname,
            user=user,
            passwd=password,
            host=host,
            port=port)
    except Exception as e:
        print(e)
        sys.exit(1)

    sys.exit(0)

if __name__ == "__main__":
    database_check()
