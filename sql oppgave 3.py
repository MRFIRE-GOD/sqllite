import sqlite3
import csv
import os

global cur
global conn 

def tabel(): 
    global conn
    conn = sqlite3.connect ("nummer.db")
    
    global cur
    cur.execute("""CREATE TABLE fname TEXT, ename TEXT,  """)