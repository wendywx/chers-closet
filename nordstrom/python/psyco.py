#!/usr/bin/python

import psycopg2
from config import config


def create_tables():
	commands = (
		"""
		CREATE TABLE products(
			brand TEXT, 
			color VARCHAR(30),
			gender VARCHAR(10),
			imgUrl TEXT,
			price INTEGER, 
			productId INTEGER,
			rating FLOAT(2)
		)
""",
"""
		CREATE TABLE brands(
			brand TEXT ,
			occasion VARCHAR(30)
		)
""",
"""
		CREATE TABLE types(
			season VARCHAR(10),
			typeName VARCHAR(30),
			parentType VARCHAR(20)
		)
""",
"""
		CREATE TABLE products(
			brand TEXT ,
			color VARCHAR(30),
			gender VARCHAR(10),
			imgUrl TEXT,
			price INTEGER, 
			productId INTEGER,
			rating FLOAT(2)
		)
""",
"""
		CREATE TABLE closets(
			closetId INTEGER,
			closetName TEXT
		)
""",
"""
		CREATE TABLE users(
			userId INTEGER,
			fName TEXT,
			lName TEXT,
			closetId INTEGER
		)
""")

	conn = None
	try: 
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		for command in commands:
			cur.execute(command)
		cur.close()
		conn.commit()
	except(Exception, psycopg2.DatabaseError) as error:
		print(error)

	finally:
		if conn is not None:
			conn.close()

create_tables()
