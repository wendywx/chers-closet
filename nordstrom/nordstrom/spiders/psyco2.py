#!/usr/bin/python

import psycopg2

try:
	conn = psycopg2.connect(database = "annapelleti", user = "annapelleti", password = "pass123", host = "localhost", port = "5432")
except:
	print("unable to open database")
#print("opened database successfuly")

cur = conn.cursor()


cur.execute('''
		CREATE TABLE brands(
			brand TEXT ,
			occasion VARCHAR(30)
		);
''')
cur.execute('''
		CREATE TABLE types(
			season VARCHAR(10),
			typeName VARCHAR(30),
			parentType VARCHAR(20)
		);
''')

cur.execute('''
		CREATE TABLE closets(
			closetId INTEGER,
			closetName TEXT
		);'''
)

cur.execute('''
		CREATE TABLE users(
			userId INTEGER,
			fName TEXT,
			lName TEXT,
			closetId INTEGER
		);'''

)

print("table created successfully")
conn.commit()
conn.close()