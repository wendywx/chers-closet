#!/usr/bin/python

import psycopg2

try:
	conn = psycopg2.connect(database = "annapelleti", user = "annapelleti", password = "pass123", host = "localhost", port = "5432")
except:
	print("unable to open database")
#print("opened database successfuly")

cur = conn.cursor()

f = open("data.txt",'r')
for line in f:
	a = line.split(",")
	if len(a) == 10:
		count = 0
		for attrib in a:
			if attrib != 'null':
				if(count is 2):
					attrib = attrib.split("–")				
					attrib = attrib[0].replace('\"', "")
					attrib = attrib.replace('$', "")
					attrib = int(attrib.replace('.00', ''))
					a[count] = attrib

				elif(count is 0):
					attrib = float(attrib)
					a[count] = attrib
				elif(count is 4):
					attrib = int(attrib)
					a[count] = attrib
				else:
					attrib = attrib.replace('\"','')
					a[count] = attrib
				count += 1

	rating = a[0]
	color = a[1]
	price = a[2]
	brand = a[3]
	product_id = a[4]
	product_name = a[5]
	gender = a[6]
	product_type = a[7]
	parent = a[8]
	imgurl = a[9]

	cur.execute('''
		INSERT INTO products(brand,color,gender,imgurl,price,productid,rating,productname)
		VALUES (%s,%s,%s,%s,%s,%s,%s,%s);''', (brand,color,gender,imgurl,price,product_id,rating,product_name))

	cur.execute('''
		INSERT INTO types(season,typename,parenttype)
		VALUES (%s,%s,%s);''', ('null',product_type,parent))

	cur.execute('''
		INSERT INTO brands(brand,occasion)
		VALUES (%s,%s);''', (brand,'null'))

print("data inserted successfully")
conn.commit()
conn.close()