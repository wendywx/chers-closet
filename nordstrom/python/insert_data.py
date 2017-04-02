#!/usr/bin/python

import psycopg2

try:
	conn = psycopg2.connect(database = "Wendy", user = "Wendy", password = "pass123", host = "localhost", port = "5432")
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
			if(count is 2):
				if attrib != 'null':
					attrib = attrib.split("–")				
					attrib = attrib[0].replace('\"', "")
					attrib = attrib.replace('$', "")
					attrib = float(attrib)
				else:
					attrib = -1
				a[count] = attrib
			elif(count is 0):
				if attrib != 'null':
					attrib = float(attrib)
				else:
					attrib = -1.0
				a[count] = attrib
			elif(count is 4):
				if attrib != 'null':
					attrib = int(attrib)
				else:
					attrib = -1
				a[count] = attrib
			else:
				if attrib != 'null':
					attrib = attrib.replace('\"','')
				a[count] = attrib
			count += 1

		rating = a[0]
		brand = a[1]
		price = a[2]
		color = a[3]
		product_id = a[4]
		product_name = a[5]
		gender = a[6]
		product_type = a[7]
		parent = a[8]
		img_url = a[9]

		cur.execute("""
			INSERT INTO types(typeName,parentType,season)
			VALUES ('{0}',{1},{2})
			ON CONFLICT DO NOTHING;
		""".format(product_type,'null','null'))

		cur.execute("""
			INSERT INTO products(productId,productName,productType,brand,color,gender,price,rating,imgurl)
			VALUES ({0},'{1}','{2}','{3}','{4}','{5}',{6},{7},'{8}')
			ON CONFLICT DO NOTHING;
		""".format(product_id,product_name,product_type,brand,color,gender,price,rating,img_url))
		


print("data inserted successfully")
conn.commit()
conn.close()