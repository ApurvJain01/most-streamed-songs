'''
This file will be used to read data from csv file using pandas module .
'''
import pandas as pd
from sqlalchemy import create_engine


# Creating a data frane
df_list_of_songs = pd.read_csv('most_streamed_spotify_songs_2024.csv', header = 0, encoding= 'unicode_escape')
print (df_list_of_songs.to_string())

# move data to mysql 
# Creating connection to mysql databaase 

db_connection = sqlalchemy.create_engine('mysql+mysqlconnector://root:SuperSecret@passwd123@localhost/most_streamed_songs')