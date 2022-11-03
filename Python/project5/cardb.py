#Nabeel Latifi
#I nabeel latifi am the author of this work
"""import csv into db"""
import sqlite3
import pandas as pd
con = sqlite3.connect("car.sqlite3")
car_data = pd.read_csv("cars2.csv")
car_data.to_sql('cars', con, if_exists='replace', index=False)

c = con.execute("SELECT * FROM userinfo")
for item in c:
    print(item)
con.close()

# ///SELECT *
# FROM movies
# WHERE imdb_rating > 8;

# SELECT * 
# FROM movies
# WHERE name LIKE 'Se_en';