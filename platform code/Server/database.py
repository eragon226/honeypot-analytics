import sqlite3 as lite
import sys

def setup():
    con = lite.connect('malware.db')

    with con:
        
        cur = con.cursor()    
        cur.execute("""CREATE TABLE IF NOT EXISTS Samples(
            HASH TEXT,
            SIZE TEXT , 
            FILE_MOD_TIME TEXT,
            FILE_TYPE TEXT,
            MIME_TYPE TEXT)""")
    return con

def connect():
    return lite.connect('malware.db')