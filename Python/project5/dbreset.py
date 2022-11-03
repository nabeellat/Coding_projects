# MCS 275 Spring 2021 Lecture 38
# Code Provided by Professor Dumas
"""Database reset"""
import sqlite3
import sys

DBFILE = "car.sqlite3"

con = sqlite3.connect(DBFILE)

print("Resetting database '{}'".format(DBFILE))

# delete messages table
con.execute("""
DROP TABLE IF EXISTS cars;""")
con.execute("""DROP TABLE IF EXISTS userinfo;""")
# create messages table
con.execute("""
CREATE TABLE cars (
    Car TEXT,
    mpg DOUBLE,
    Cylinders INTEGER,
    Displacement DOUBLE,
    Horsepower DOUBLE,
    Weight DOUBLE,
    Acceleration INTEGER,
    Orgin TEXT
);
""")

con.execute("CREATE TABLE userinfo(username TEXT,password TEXT);")
con.execute("INSERT INTO userinfo(username,password) VALUES('Nabeel','cool99');")
con.commit()
con.close()