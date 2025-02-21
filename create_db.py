import sqlite3 as sql

#connect to SQLite
con = sql.connect('db_web.db')

#Create a Connection
cur = con.cursor()

#Drop users table if already exsist.
cur.execute("DROP TABLE IF EXISTS notes")

#Create users table  in db_web database
sql ='''CREATE TABLE "notes" (
	"ID"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"Título"	TEXT,
	"Detalhes"	TEXT
)'''
cur.execute(sql)

#commit changes
con.commit()

#close the connection
con.close()