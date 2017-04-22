#!/usr/bin/python

import psycopg2


def delete_tables():
	commands = (
		"DROP TABLE types CASCADE;",
		"DROP TABLE products CASCADE;"
		"DROP TABLE closets CASCADE;",
		"DROP TABLE outfits CASCADE;",
		)
	dbname = input("Enter a database name: ")
	user = input("Enter user name: ")
	conn = None
	try: 
		conn = psycopg2.connect(database = dbname, user = user, password = "pass123", host = "localhost", port = "5432")
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


delete_tables()
print("all tables deleted successfully")
