#!/usr/bin/python

import psycopg2

dbname = input("Enter a database name: ")
user = input("Enter user name: ")
try:

	conn = psycopg2.connect(database =dbname, user = user, password = "pass123", host = "localhost", port = "5432")
except:
	print("unable to open database")

cur = conn.cursor()

tops = ["tops","tank/cami/shell", "t-shirt/tee", "shirt", "polo", "sweater", \
"camisole", "blouse/top", "sweatshirt", "sweatshirt/hoody/zipfront",\
"tunic", "shirtjacket", "swim top", "dress-shirt","sportshirt", "onesie", "sweatsuit/warm-ups"]

bottoms = ["bottoms", "short", "stirrup/legging", "pant", "skirt"]

dresses = ["dresses", "dress", "jumpsuit/romper","skirt set"]

outerwear = ["outerwear","jacket", "blazer", "short jacket/coat", "jacket/coat", \
"3/4 or long coat", "anorak/parka", "sportcoat", "vest", "raincoat",\
"poncho/cape", "bolero",]

shoes = ["shoes","sneaker", "flats", "sandals/slides", "loafers", "boots","pumps",\
"athletic", "mule","clog","slip on","slippers","oxfords"]

junk = ["waist support/band", "panty/brief", "shoe tree","polish",
"insoles","brush"]

parenttypes = [tops, bottoms, dresses, outerwear, shoes]


dressy = ["dressy","onesie","skirt","dress","jumpsuit/romper","skirt set","3/4 or long coat","vest", \
"bolero","sandals/slides","pumps","mule",]

work = ["work","blouse/top","dress-shirt","pant","blazer","sportcoat","flats","loafers","oxfords"]

casual = ["casual","tank/cami/shell","shirt","polo","sweater","camisole","sweatshirt","tunic", \
"shirtjacket","short","jacket","short jacket/coat","anorak/parka","raincoat","poncho/cape", \
"sneaker","boots""clog","slip on","slippers"]

athletic = ["athletic","t-shirt/tee","sweatshirt/hoody/zipfront","swim top","sportshirt", \
"sweatsuit/warm-ups","stirrup/legging","athletic",]

occasions = [dressy, work, casual, athletic]


fall = ["fall","t-shirt/tee","shirt","polo","sweater","blouse/top","sweatshirt","sweatshirt/hoody/zipfront", \
"tunic","shirtjacket","dress-shirt","sportshirt","sweatsuit/warm-ups","stirrup/legging","pant", \
"skirt","dress","jumpsuit/romper","skirt set","jacket","blazer","jacket/coat", \
"3/4 or long coat","anorak/parka","sportcoat","vest","raincoat","poncho/cape","sneaker","flats", \
"loafers","boots","pumps","athletic","mule","clog","slip on","slippers","oxfords"]

winter = ["wint","shirt","sweater","sweatshirt""sweatshirt/hoody/zipfront","dress-shirt","sportshirt", \
"stirrup/legging","pant","jacket","blazer","jacket/coat","3/4 or long coat","sportcoat","raincoat", \
"sneaker","loafers","boots","pumps","athletic","oxfords"]

spring = ["spr", "tank/cami/shell","tops","t-shirt/tee","shirt","polo","blouse/top","sweatshirt/hoody/zipfront", \
"tunic","shirtjacket","dress-shirt","sportshirt","sweatsuit/warm-ups","short","stirrup/legging", \
"pant","skirt","dress","jumpsuit/romper","skirt set","blazer","short jacket/coat", \
"jacket/coat","anorak/parka","sportcoat","vest","raincoat","poncho/cape","bolero","sneaker","flats", \
"sandals/slides","loafers","pumps","athletic","mule","slip on","slippers","oxfords"]

summer = ["sum","tank/cami/shell","t-shirt/tee","shirt","polo","camisole","blouse/top","tunic","swim top", \
"dress-shirt","sportshirt","onesie","sweatsuit/warm-ups","short","skirt","dress","jumpsuit/romper", \
"skirt set","blazer","short jacket/coat","sportcoat","vest","raincoat","poncho/cape","bolero","sneaker", \
"flats","sandals/slides","pumps","athletic","mule","clog","slip on","oxfords"]

seasons = [fall, spring, summer, winter]



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


		for ptype in parenttypes:
			if product_type.lower() in ptype:
				parent_type = ptype[0]
		
		for occasion in occasions:
			if product_type.lower() in occasion:
				occasion_type = occasion[0]

		product_seasons = ""
		for season in seasons:
			if product_type.lower() in season:
				product_seasons += season[0]

		cur.execute("""
		 	INSERT INTO types(typeName,parentType,season,occasion)
		 	VALUES ('{0}','{1}','{2}','{3}')
		 	ON CONFLICT DO NOTHING;
		""".format(product_type, parent_type, product_seasons, occasion_type))

		# cur.execute("""
		# 	INSERT INTO products(productId,productName,productType,brand,color,gender,price,rating,imgurl)
		# 	VALUES ({0},'{1}','{2}','{3}','{4}','{5}',{6},{7},'{8}')
		# 	ON CONFLICT DO NOTHING;
		# """.format(product_id,product_name,product_type,brand,color,gender,price,rating,img_url))
		


print("data inserted successfully")
conn.commit()
conn.close()