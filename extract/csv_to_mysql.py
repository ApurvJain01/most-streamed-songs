
from mysql.connector.pooling import MySQLConnectionPool
import json
import logging

with open('config.json', 'r') as connection_config:
    config = json.load(connection_config)


def get_connection(): 
    pool = MySQLConnectionPool(**config)
    connection = pool.get_connection()
    return connection

# sql = "show databases;"

def query_database():
    connection = get_connection()
    cursor = connection.cursor()
    # cursor.execute(sql)
    # Read the sql file
    fd = open('sql/create_schema.sql', 'r')
    sqlFile = fd.read()
    fd.close()
 
    # SQL commands
    sqlCommands = sqlFile.split(';')

    for cmd in sqlCommands:
        try:
            cursor.execute(cmd)
        except: 
            logging.error("The command is not executed!!!")
    result = cursor.fetchall()
    cursor.close()
    connection.close()
    return result

print(f"This is the list of databases on server:  ${query_database()}")

# need to create a function to create a table in database from this csv data. 