import sqlite3 as lite
import sys
import web

def add(con, data):
	web.debug(data)
	with con:
		cur = con.cursor()
		cur.execute("INSERT INTO Samples VALUES(?,?,?,?,?)",data)
	return