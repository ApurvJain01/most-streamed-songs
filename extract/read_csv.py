'''
This file will be used to read data from csv file using pandas module .
'''
import pandas as pd
import csv_to_mysql
from mysql.connector.pooling import MySQLConnectionPool
import json

csv_file_path = 'most_streamed_spotify_songs_2024.csv'
table_name='2024_spotify_most_streamed_songs'


with open('config.json', 'r') as connection_config:
    config = json.load(connection_config)

def get_connection(): 
    pool = MySQLConnectionPool(**config)
    connection = pool.get_connection()
    return connection


def csv_to_df(csv_file_path):
    # Creating a data frane
    df_list_of_songs = pd.read_csv(csv_file_path , header = 0, encoding= 'unicode_escape')
    # print (df_list_of_songs.iloc[0,:])
    print (df_list_of_songs.columns)
    columns = df_list_of_songs.columns
    df_list_of_songs.to_sql(table_name, get_connection(), index=False)
    return columns

# need to add function which returns a datafrane 