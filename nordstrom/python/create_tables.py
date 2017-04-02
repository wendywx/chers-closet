#!/usr/bin/python

import psycopg2

def create_tables():
	commands = (
		"""
		CREATE TABLE types(
			typeName TEXT PRIMARY KEY,
			parentType VARCHAR(20),
			season VARCHAR(20),
			occasion VARCHAR(30)
		)
""",
"""
		CREATE TABLE products(
			productId INTEGER PRIMARY KEY,
			productName TEXT,
			productType TEXT REFERENCES types (typeName),
			brand TEXT, 
			color TEXT,
			gender VARCHAR(10),
			price FLOAT(2), 
			rating FLOAT(2),
			imgUrl TEXT
		)
""",
"""
		CREATE TABLE outfits(
			outfitId INTEGER PRIMARY KEY,
			top INTEGER REFERENCES products (productId),
			bottom INTEGER REFERENCES products (productId),
			shoes INTEGER REFERENCES products (productId)
		)
""",
"""
		CREATE TABLE closets(
			closetId INTEGER PRIMARY KEY,
			product1 INTEGER REFERENCES products (productId),
			product2 INTEGER REFERENCES products (productId),
			product3 INTEGER REFERENCES products (productId),
			product4 INTEGER REFERENCES products (productId),
			product5 INTEGER REFERENCES products (productId),
			product6 INTEGER REFERENCES products (productId),
			product7 INTEGER REFERENCES products (productId),
			product8 INTEGER REFERENCES products (productId),
			product9 INTEGER REFERENCES products (productId),
			product10 INTEGER REFERENCES products (productId),
			product11 INTEGER REFERENCES products (productId),
			product12 INTEGER REFERENCES products (productId),
			product13 INTEGER REFERENCES products (productId),
			product14 INTEGER REFERENCES products (productId),
			product15 INTEGER REFERENCES products (productId),
			product16 INTEGER REFERENCES products (productId),
			product17 INTEGER REFERENCES products (productId),
			product18 INTEGER REFERENCES products (productId),
			product19 INTEGER REFERENCES products (productId),
			product20 INTEGER REFERENCES products (productId),
			product21 INTEGER REFERENCES products (productId),
			product22 INTEGER REFERENCES products (productId),
			product23 INTEGER REFERENCES products (productId),
			product24 INTEGER REFERENCES products (productId),
			product25 INTEGER REFERENCES products (productId),
			product26 INTEGER REFERENCES products (productId),
			product27 INTEGER REFERENCES products (productId),
			product28 INTEGER REFERENCES products (productId),
			product29 INTEGER REFERENCES products (productId),
			product30 INTEGER REFERENCES products (productId),
			product31 INTEGER REFERENCES products (productId),
			product32 INTEGER REFERENCES products (productId),
			product33 INTEGER REFERENCES products (productId),
			product34 INTEGER REFERENCES products (productId),
			product35 INTEGER REFERENCES products (productId),
			product36 INTEGER REFERENCES products (productId),
			product37 INTEGER REFERENCES products (productId),
			product38 INTEGER REFERENCES products (productId),
			product39 INTEGER REFERENCES products (productId),
			product40 INTEGER REFERENCES products (productId),
			product41 INTEGER REFERENCES products (productId),
			product42 INTEGER REFERENCES products (productId),
			product43 INTEGER REFERENCES products (productId),
			product44 INTEGER REFERENCES products (productId),
			product45 INTEGER REFERENCES products (productId),
			product46 INTEGER REFERENCES products (productId),
			product47 INTEGER REFERENCES products (productId),
			product48 INTEGER REFERENCES products (productId),
			product49 INTEGER REFERENCES products (productId),
			product50 INTEGER REFERENCES products (productId),
			outfit1 INTEGER REFERENCES outfits (outfitId),
			outfit2 INTEGER REFERENCES outfits (outfitId),
			outfit3 INTEGER REFERENCES outfits (outfitId),
			outfit4 INTEGER REFERENCES outfits (outfitId),
			outfit5 INTEGER REFERENCES outfits (outfitId),
			outfit6 INTEGER REFERENCES outfits (outfitId),
			outfit7 INTEGER REFERENCES outfits (outfitId),
			outfit8 INTEGER REFERENCES outfits (outfitId),
			outfit9 INTEGER REFERENCES outfits (outfitId),
			outfit10 INTEGER REFERENCES outfits (outfitId)
		)
""",
"""
		CREATE TABLE users(
			userId INTEGER PRIMARY KEY,
			fName TEXT,
			lName TEXT,
			closetId INTEGER REFERENCES closets (closetId)
		)
""")

	conn = None
	dbname = input("Enter a database name: ")
	user = input("Enter user name: ")
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

create_tables()
print("all tables created successfully")
