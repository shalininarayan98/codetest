from pathlib import Path
import sqlite3
import pandas as pd
from sqlite3 import Error
from sqlalchemy import create_engine
import os
import sys
from table import sqlite_table
from q1 import question_one
from q2 import question_two
from q3 import question_three
from decouple import config

FilePath= config('LOCATION')

conn = sqlite3.connect('my_data.db')
Path('my_data.db').touch()
c = conn.cursor()

def sqlite_connection():
    try:
        conn = sqlite3.connect('my_data.db')
        print("Successfully connected to db")
        return conn
    except Error:
        print(Error)

#sqlite_connection()

c.execute('''DROP TABLE test''')

conn = sqlite_connection()

sqlite_table(conn)

test = pd.read_csv(FilePath)

test.to_sql('test', conn, if_exists='append', index = False)

def sqlite_q1():
    try:
        value1 = question_one(conn)
        print("Successfully returned output for question 1. Please find the output in '/Users/shalini/Documents/testoutput1.json' ")
        return conn
    except Error:
        print(Error)

def sqlite_q2():
    try:
        value2 = question_two(conn)
        print("Successfully returned output for question 2. Please find the output in '/Users/shalini/Documents/testoutput2.json' ")
        return conn
    except Error:
        print(Error)

def sqlite_q3():
    try:
        value3 = question_three(conn)
        print("Successfully returned output for question 3. Please find the output in '/Users/shalini/Documents/testoutput3.json' ")
        return conn
    except Error:
        print(Error)

sqlite_q1()
sqlite_q2()
sqlite_q3()