import random

from django.shortcuts import render
from django.http import HttpResponse

from .models import Product, Closet, Type, Outfit

def home(request):
	return render(request, 'home.html', {})

def view_outfits(request):
	return render(request, 'view_outfits.html', {})

def view_products(request):
	return render(request, 'view_products.html', {})

def findprodattrib(productid, attribname):
	myattrib_q = Product.objects.filter(productid=productid).values(attribname)
	myattrib = myattrib_q[0][attribname]
	return myattrib


def findtypeattrib(mytypename, attribname):
	myattrib_q = Type.objects.filter(typename=mytypename).values(attribname)
	myattrib = myattrib_q[0][attribname]
	return myattrib

def findoutfitprod(myoutfitid, product):
	myattrib_q = Outfit.objects.filter(outfitid=myoutfitid).values(product)
	if myattrib_q.exists():
		myattrib = myattrib_q[0][product]
	else:
		print(product + " is not included in this outfit")
		myattrib = None
	return myattrib

def generate_product(query, myseason, myoccasion):
	product = list(query.values_list(flat=True)) #generate random products

	if len(product) > 0:
		if len(myseason) == 0 and len(myoccasion) == 0:
			rand_num = random.randint(0,len(product)-1)
			myproduct = product[rand_num]#pid

		else:
			if len(myseason) == 0:
				seasonflag = 1
			else:
				seasonflag = 0

			if len(myoccasion) == 0:
				occasionflag = 1
			else:
				occasionflag = 0

			myproduct = 0

			print('seasonflag')
			print(seasonflag)
			print('occasionflag')
			print(occasionflag)

			season_flag = 0
			occasion_flag = 0

			while season_flag != 1 or occasion_flag != 1:
				if seasonflag == 1:
					season_flag = seasonflag
				else:
					season_flag = 0

				if occasionflag == 1:
					occasion_flag = occasionflag
				else:
					occasion_flag = 0

				rand_num = random.randint(0,len(product)-1)
				myproduct = product[rand_num]#pid
				producttype = findprodattrib(myproduct, 'producttype')
				productseason = findtypeattrib(producttype, 'season').split(':')
				productoccasion = findtypeattrib(producttype, 'occasion').split(':')

				for i in productseason:
					if i in myseason:
						season_flag = 1

				for j in productoccasion:
					if j in myoccasion:
						occasion_flag = 1

		productimgurl = findprodattrib(myproduct, 'imgurl')
		brand = findprodattrib(myproduct,'brand')
		name = findprodattrib(myproduct,'productname')
		pid = findprodattrib(myproduct, 'productid')
		price = findprodattrib(myproduct, 'price')
		return [productimgurl, brand, name, pid, price]
	else:
		print("something is wrong inside generate product")
		return [0]


def browse_products(request):
	junk = ["Shoe tree", "Polish", "Insoles", "Brush"]
	types = list(Type.objects.order_by('typename').all().values_list('typename', flat=True))
	for i in junk:
		types.remove(i)
	brands = Product.objects.order_by('brand').values_list('brand', flat=True).distinct()
	prices = ['$0-$50','$50-$100', '$100-$200', '$200-$400','$400-$1000']
	gender = ['Male', 'Female']
	result = [types, brands, prices, gender]
	return render(request, 'browse_products.html', {"results": result})


def browse_outfits(request):
	season = ['Fall', 'Spring', 'Summer', 'Winter']
	occasion = ['Athletic', 'Casual', 'Dressy', 'Work']
	totalprice = ['$0-$300','$300-$600', '$600-$900', '$900-$1200', '$1200-$1500', '$1500-$1800','$2100-$3000','$3000-$5000']
	gender = ['Male', 'Female']
	result = [season, occasion, totalprice, gender]
	return render(request, 'browse_outfits.html', {"results": result})


def product_results(request):
	return render(request, 'product_results.html', {})


def outfit_results(request):
	return render(request, 'outfit_results.html', {})


def added_to_closet(request):
	return render(request, "added_to_closet.html", {})


def view_closet(request):
	return render(request, "view_closet.html", {})


def generateOutfitFromProduct(mypid):
	#modify to return a list of imgurls, brands and names
	result = []
	imgurls = []
	brands = []
	names =[]
	pids = []
	prices = []
	totalprice = 0

	tops = list(Type.objects.filter(parenttype="tops").values_list(flat=True))
	bottoms = list(Type.objects.filter(parenttype="bottoms").values_list(flat=True))
	outerwear = list(Type.objects.filter(parenttype="outerwear").values_list(flat=True))
	shoes = list(Type.objects.filter(parenttype="shoes").values_list(flat=True))
	dresses = list(Type.objects.filter(parenttype="dresses").values_list(flat=True))

	name = findprodattrib(mypid, 'productname')
	myimgurl = findprodattrib(mypid, 'imgurl')
	myproducttype = findprodattrib(mypid, 'producttype')
	mygender = findprodattrib(mypid, 'gender')
	myparenttype = findtypeattrib(myproducttype, 'parenttype')
	myprice = findprodattrib(mypid, 'price')
	myoccasion = findtypeattrib(myproducttype, 'occasion').split(':')
	myseason = findtypeattrib(myproducttype, 'season').split(':')
	myproducts_q = Product.objects.filter(gender=mygender)

	# filter down to type
	tops_q = myproducts_q.filter(producttype__in=tops)
	bottoms_q = myproducts_q.filter(producttype__in=bottoms)
	dresses_q = myproducts_q.filter(producttype__in=dresses)
	shoes_q = myproducts_q.filter(producttype__in=shoes)
	outerwear_q = myproducts_q.filter(producttype__in=outerwear)

	# 5 possible parenttype choices, generate random parenttypes based on our already filtered queries
	if(myparenttype == "tops"): 

		generated_outerwear = generate_product(outerwear_q, myseason, myoccasion) #generate outerwear
		if len(generated_outerwear) > 1:
			imgurls.append(generated_outerwear[0])
			brands.append(generated_outerwear[1])
			names.append(generated_outerwear[2])
			pids.append(generated_outerwear[3])
			prices.append(generated_outerwear[4])

		topimgurl = findprodattrib(mypid,'imgurl') #user chosen top
		brand = findprodattrib(mypid,'brand')
		name = findprodattrib(mypid,'productname')
		pid = findprodattrib(mypid, 'productid')
		price = findprodattrib(mypid,'price')
		imgurls.append(topimgurl)	
		brands.append(brand)
		names.append(name)
		pids.append(pid)
		prices.append(price)

		generated_bottom = generate_product(bottoms_q, myseason, myoccasion) #generate bottom
		imgurls.append(generated_bottom[0])
		brands.append(generated_bottom[1])
		names.append(generated_bottom[2])
		pids.append(generated_bottom[3])
		prices.append(generated_bottom[4])

		generated_shoes = generate_product(shoes_q, myseason, myoccasion) #generate top
		imgurls.append(generated_shoes[0])
		brands.append(generated_shoes[1])
		names.append(generated_shoes[2])
		pids.append(generated_shoes[3])
		prices.append(generated_shoes[4])

	elif(myparenttype == "bottoms"): 

		generated_outerwear = generate_product(outerwear_q, myseason, myoccasion) #generate outerwear
		if len(generated_outerwear) > 1:
			imgurls.append(generated_outerwear[0])
			brands.append(generated_outerwear[1])
			names.append(generated_outerwear[2])
			pids.append(generated_outerwear[3])
			prices.append(generated_outerwear[4])

		generated_top = generate_product(tops_q, myseason, myoccasion) #generate top
		imgurls.append(generated_top[0])
		brands.append(generated_top[1])
		names.append(generated_top[2])
		pids.append(generated_top[3])
		prices.append(generated_top[4])

		bottomimgurl = findprodattrib(mypid,'imgurl') #user chosen bottom
		brand = findprodattrib(mypid,'brand')
		name = findprodattrib(mypid,'productname')
		pid = findprodattrib(mypid, 'productid')
		price = findprodattrib(mypid,'price')
		imgurls.append(bottomimgurl)
		brands.append(brand)
		names.append(name)
		pids.append(pid)
		prices.append(price)

		generated_shoes = generate_product(shoes_q, myseason, myoccasion) #generate shoes
		imgurls.append(generated_shoes[0])
		brands.append(generated_shoes[1])
		names.append(generated_shoes[2])
		pids.append(generated_shoes[3])
		prices.append(generated_shoes[4])

	elif(myparenttype == "outerwear"): 

		outerwearimgurl = findprodattrib(mypid,'imgurl') #user chosen outerwear
		imgurls.append(outerwearimgurl)
		brand = findprodattrib(mypid,'brand')
		name = findprodattrib(mypid,'productname')	
		pid = findprodattrib(mypid, 'productid')
		price = findprodattrib(mypid,'price')
		brands.append(brand)
		names.append(name)
		pids.append(pid)
		prices.append(price)

		if 'dressy' in myoccasion: #since dresses are categorized only as dressy
			if random.randint(0,1) == 0: #randomly choose whether to match outerwear with dress or with top/bottom
				generated_top = generate_product(tops_q, myseason, myoccasion)
				imgurls.append(generated_top[0])
				brands.append(generated_top[1])
				names.append(generated_top[2])
				pids.append(generated_top[3])
				prices.append(generated_top[4])

				generated_bottom = generate_product(bottoms_q, myseason, myoccasion)
				imgurls.append(generated_bottom[0])
				brands.append(generated_bottom[1])
				names.append(generated_bottom[2])
				pids.append(generated_bottom[3])
				prices.append(generated_bottom[4])

			else:
				generated_dress = generate_product(dresses_q, myseason, myoccasion)
				imgurls.append(generated_dress[0])
				brands.append(generated_dress[1])
				names.append(generated_dress[2])
				pids.append(generated_dress[3])
				prices.append(generated_dress[4])

		else: 
			generated_top = generate_product(tops_q, myseason, myoccasion)
			imgurls.append(generated_top[0])
			brands.append(generated_top[1])
			names.append(generated_top[2])
			pids.append(generated_top[3])
			prices.append(generated_top[4])

			generated_bottom = generate_product(bottoms_q, myseason, myoccasion)
			imgurls.append(generated_bottom[0])
			brands.append(generated_bottom[1])
			names.append(generated_bottom[2])
			pids.append(generated_bottom[3])
			prices.append(generated_bottom[4])

		generated_shoes = generate_product(shoes_q, myseason, myoccasion)
		imgurls.append(generated_shoes[0])
		brands.append(generated_shoes[1])
		names.append(generated_shoes[2])
		pids.append(generated_shoes[3])
		prices.append(generated_shoes[4])

	elif(myparenttype == "dresses"): 

		generated_outerwear = generate_product(outerwear_q, myseason, myoccasion) #generate outerwear
		if len(generated_outerwear) > 1:
			imgurls.append(generated_outerwear[0])
			brands.append(generated_outerwear[1])
			names.append(generated_outerwear[2])
			pids.append(generated_outerwear[3])
			prices.append(generated_outerwear[4])

		#user input dress
		dressimgurl = findprodattrib(mypid,'imgurl')
		imgurls.append(dressimgurl)
		brand = findprodattrib(mypid,'brand')
		name = findprodattrib(mypid,'productname')
		pid = findprodattrib(mypid, 'productid')
		price = findprodattrib(mypid, 'price')
		brands.append(brand)
		names.append(name)
		pids.append(pid)
		prices.append(price)

		generated_shoes = generate_product(shoes_q, myseason, myoccasion)
		imgurls.append(generated_shoes[0])
		brands.append(generated_shoes[1])
		names.append(generated_shoes[2])
		pids.append(generated_shoes[3])
		prices.append(generated_shoes[4])

	elif(myparenttype == "shoes"):

		generated_outerwear = generate_product(outerwear_q, myseason, myoccasion)
		if len(generated_outerwear) > 1:
			imgurls.append(generated_outerwear[0])
			brands.append(generated_outerwear[1])
			names.append(generated_outerwear[2])
			pids.append(generated_outerwear[3])
			prices.append(generated_outerwear[4])

		dress = list(dresses_q.values_list(flat=True)) #generate random dress
		if 'dressy' in myoccasion:
			if random.randint(0,1) == 0: #randomly choose whether to match outerwear with dress or with top/bottom
				generated_top = generate_product(tops_q, myseason, myoccasion)
				imgurls.append(generated_top[0])
				brands.append(generated_top[1])
				names.append(generated_top[2])
				pids.append(generated_top[3])
				prices.append(generated_top[4])

				generated_bottom = generate_product(bottoms_q, myseason, myoccasion)
				imgurls.append(generated_bottom[0])
				brands.append(generated_bottom[1])
				names.append(generated_bottom[2])
				pids.append(generated_bottom[3])
				prices.append(generated_bottom[4])

			else:
				generated_dress = generate_product(dresses_q, myseason, myoccasion)
				imgurls.append(generated_dress[0])
				brands.append(generated_dress[1])
				names.append(generated_dress[2])
				pids.append(generated_dress[3])
				prices.append(generated_dress[4])

		else:	
			generated_top = generate_product(tops_q, myseason, myoccasion)
			imgurls.append(generated_top[0])
			brands.append(generated_top[1])
			names.append(generated_top[2])
			pids.append(generated_top[3])
			prices.append(generated_top[4])

			generated_bottom = generate_product(bottoms_q, myseason, myoccasion)
			imgurls.append(generated_bottom[0])
			brands.append(generated_bottom[1])
			names.append(generated_bottom[2])
			pids.append(generated_bottom[3])
			prices.append(generated_bottom[4])

		#user input shoes
		shoesimgurl = findprodattrib(mypid, 'imgurl')
		imgurls.append(shoesimgurl)
		brand = findprodattrib(mypid,'brand')
		name = findprodattrib(mypid,'productname')
		pid = findprodattrib(mypid, 'productid')
		price = findprodattrib(mypid, 'price')
		brands.append(brand)
		names.append(name)
		pids.append(pid)
		prices.append(price)

	else:
		print("error: something is wrong with parenttype")

	totalprice = 0
	for k in prices:
		totalprice += k
	result =[imgurls, brands, names, pids, prices, totalprice]
	return result


def createMyOutfit(request):
	pidList = request.GET.getlist('pids[]')
	myclosetid = request.GET.get('closetid')
	result = []

	for pid in pidList:
		image_query = Product.objects.filter(productid=pid).values('imgurl')
		imgurl = image_query[0]['imgurl']
		result.append(imgurl)		

	return render(request, "create_my_outfit.html", {"results": result})


def create_my_outfit(request):
	return render(request, "create_my_outfit.html", {})


def createNewOutfit(request):
	addedproductid = request.GET.get('newproductid')

	outfitinfo = generateOutfitFromProduct(addedproductid)
	# pids are the last of the outfitinfo 
	result = outfitinfo
	result.append(addedproductid)

	return render(request, "create_new_outfit.html", {"results": result})


def addToCloset(request):
	addedproductid = request.GET.get('newproductid')
	myclosetid = request.GET.get('closetid')
	productname = findprodattrib(addedproductid, 'productname')
	imgurl = findprodattrib(addedproductid, 'imgurl')

	#see if closet has been created
	closet_query=Closet.objects.filter(closetid=myclosetid).values('product1')

	mycloset, created = Closet.objects.update_or_create(closetid=myclosetid, defaults={'closetid':myclosetid})
	if(created):
		null_closet(myclosetid)

	added = addProductToCloset(addedproductid, myclosetid)

	if added == 0:
		print("closet full, add failed")
		result = ["Closet is full, product add failed"]
	else:
		result = ["Succesfully added " + productname + " to Closet " + myclosetid, imgurl, myclosetid]
	return render(request, "added_to_closet.html", {"results": result})

#assuming closet iexists
def addProductToCloset(addedproductid, myclosetid):
	colnum = 1
	cname = "product" + str(colnum)
	query =  Closet.objects.filter(closetid=myclosetid).values(cname)

	pid = query[0][cname]

	#look for an empty spot
	while pid is not 0 and pid is not None and colnum < 50:
		colnum += 1
		cname = "product" + str(colnum)
		query =  Closet.objects.filter(closetid=myclosetid).values(cname)
		if(query[0][cname] is not None):
			pid =int(query[0][cname]) 

	# at the end, either exited because no space, or found an empty space
	if pid is 0:
		Closet.objects.filter(closetid=myclosetid).update(**{cname: addedproductid})
		result = 1
	else:
		print("closet is full")
		result = 0

def filterProducts(request):
	type_list = request.GET.getlist('types[]')
	brand_list = request.GET.getlist('brands[]')
	price_list = request.GET.getlist('prices[]')
	gender_list = request.GET.getlist('genders[]')
	reformatted_price_list = []

	for i in price_list:
		for char in '$':
			i = i.replace(char,'')
		reformatted_price_list.append(i.split('-'))

	result = []	
	names = []
	productids = []
	images = []
	prices = []
	brands = []

	results_query = Product.objects.none()
	results_query_1 = Product.objects.none()
	results_query_2 = Product.objects.none()
	results_query_3 = Product.objects.none()

	
	if len(gender_list) == 0:
		results_query = Product.objects.all()
	else:
		for m in gender_list:
			gender_query = Product.objects.filter(gender=m)
			results_query = results_query | gender_query

	if len(type_list) == 0:
		results_query_1 = results_query
	else:
		for i in type_list:
			types_query = results_query.filter(producttype=i)
			results_query_1 = results_query_1 | types_query

	if len(brand_list) == 0:
		results_query_2 = results_query_1
	else:
		for j in brand_list:
			brands_query = results_query_1.filter(brand=j)
			results_query_2 = results_query_2 | brands_query
	
		#results_query = results_query_1
	if len(price_list) == 0:
		results_query_3 = results_query_2
	else: 
		for k in reformatted_price_list:
			minimum = k[0]
			maximum = k[1]
			price_query = results_query_2.filter(price__range=(minimum,maximum))
			results_query_3 = results_query_3 | price_query

	results_query = results_query_3

	for product in results_query:
		names.append(product.productname)
		images.append(product.imgurl)
		prices.append(product.price)
		brands.append(product.brand)
		productids.append(product.productid)
		print(product); 

	result = [names, images, prices, brands, productids]

	return render(request, "product_results.html", {"results": result})


def filterOutfits(request):

	imgurls = []
	brands = []
	names =[]
	pids = []
	prices = []
	reformatted_season_list = []
	reformatted_occasion_list = []
	reformatted_price_list = []

	season_list = request.GET.getlist('seasons[]')
	for i in season_list:
		if i == 'Fall':
			reformatted_season_list.append('fall')
		elif i == 'Spring':
			reformatted_season_list.append('spr')
		elif i == 'Summer':
			reformatted_season_list.append('sum')
		else:
			reformatted_season_list.append('wint')
	
	occasion_list = request.GET.getlist('occasions[]')
	for j in occasion_list:
		reformatted_occasion_list.append(j.lower())
	
	price_list = request.GET.getlist('totalprices[]')
	for i in price_list:
		for char in '$':
			i = i.replace(char,'')
		reformatted_price_list.append(i.split('-'))

	gender_list = request.GET.getlist('genders[]')

	if len(gender_list) == 1:
		first_query = Product.objects.filter(gender=gender_list[0])
	else:
		first_query = Product.objects.all()

	tops = list(Type.objects.filter(parenttype="tops").values_list(flat=True))
	bottoms = list(Type.objects.filter(parenttype="bottoms").values_list(flat=True))
	outerwear = list(Type.objects.filter(parenttype="outerwear").values_list(flat=True))
	shoes = list(Type.objects.filter(parenttype="shoes").values_list(flat=True))
	dresses = list(Type.objects.filter(parenttype="dresses").values_list(flat=True))

	tops_q = first_query.filter(producttype__in=tops)
	bottoms_q = first_query.filter(producttype__in=bottoms)
	dresses_q = first_query.filter(producttype__in=dresses)
	shoes_q = first_query.filter(producttype__in=shoes)
	outerwear_q = first_query.filter(producttype__in=outerwear)

	generated_outerwear = []
	generated_top = []
	generated_bottom = []
	generated_dress = []
	generated_shoes = []

	if len(reformatted_price_list) > 0:
		minprice = int(reformatted_price_list[0][0])
		maxprice = int(reformatted_price_list[-1][1])
	else:
		minprice = 0
		maxprice = 10000

	outfitprice = -1
	while outfitprice < minprice or outfitprice > maxprice:

		outfitprice = 0
		#[productimgurl, brand, name, pid, price]

		generated_outerwear = generate_product(outerwear_q, reformatted_season_list, reformatted_occasion_list)

		if len(generated_outerwear) > 1:
			outfitprice += generated_outerwear[4]

		if 'dressy' in reformatted_occasion_list:
			if random.randint(0,1) == 0: #randomly choose whether to match outerwear with dress or with top/bottom
				generated_top = generate_product(tops_q, reformatted_season_list, reformatted_occasion_list)
				outfitprice += generated_top[4]

				generated_bottom = generate_product(bottoms_q, reformatted_season_list, reformatted_occasion_list)
				outfitprice += generated_bottom[4]

			else:
				generated_dress = generate_product(dresses_q, reformatted_season_list, reformatted_occasion_list)
				outfitprice += generated_dress[4]

		else:
			generated_top = generate_product(tops_q, reformatted_season_list, reformatted_occasion_list)
			outfitprice += generated_top[4]

			generated_bottom = generate_product(bottoms_q, reformatted_season_list, reformatted_occasion_list)
			outfitprice += generated_bottom[4]

		generated_shoes = generate_product(shoes_q, reformatted_season_list, reformatted_occasion_list)
		outfitprice += generated_shoes[4]

	if len(generated_outerwear) > 1:
		imgurls.append(generated_outerwear[0])
		brands.append(generated_outerwear[1])
		names.append(generated_outerwear[2])
		pids.append(generated_outerwear[3])
		prices.append(generated_outerwear[4])

	if len(generated_dress) > 1:
		imgurls.append(generated_dress[0])
		brands.append(generated_dress[1])
		names.append(generated_dress[2])
		pids.append(generated_dress[3])
		prices.append(generated_dress[4])
	else:
		imgurls.append(generated_top[0])
		brands.append(generated_top[1])
		names.append(generated_top[2])
		pids.append(generated_top[3])
		prices.append(generated_top[4])

		imgurls.append(generated_bottom[0])
		brands.append(generated_bottom[1])
		names.append(generated_bottom[2])
		pids.append(generated_bottom[3])
		prices.append(generated_bottom[4])

	imgurls.append(generated_shoes[0])
	brands.append(generated_shoes[1])
	names.append(generated_shoes[2])
	pids.append(generated_shoes[3])
	prices.append(generated_shoes[4])

	generatedoutfit = [imgurls, brands, names, pids, prices, outfitprice]
	generatedoutfit.append(gender_list)
	generatedoutfit.append(season_list)
	generatedoutfit.append(occasion_list)
	generatedoutfit.append(price_list)


#result =[imgurls, brands, names, pids, prices, totalprice]

	return render(request, "outfit_results.html", {"results": generatedoutfit})


def about(request):
	return render(request, 'about.html', {})


def acct_home(request):
	return render(request, 'acct_home.html', {})


def my_closet(request):
	return render(request, 'my_closet.html', {})


def contact(request):
	return render(request, 'contact.html', {})


def create_new_closet(request):
	return render(request, 'create_new_closet.html', {})


def create_new_outfit(request):
	return render(request, 'create_new_outfit.html', {})


def generate_new_outfit(request):
	return render(request, 'generate_new_outfit.html', {})


def log_in(request):
	return render(request, 'log_in.html', {})


def my_account(request):
	return render(request, 'my_account.html', {})


def register(request):
	return render(request, 'register.html', {})

def add_outfit(request):
	return render(request, 'add_outfit.html', {})


def addOutfit(request):
	myclosetid = request.GET.get('closetid')
	pids = request.GET.getlist('pids[]')
	pids = pids[0]
	pids = eval(pids)
	imgs=[]

	closet_query=Closet.objects.filter(closetid=myclosetid).values('outfit1')
	mycloset, created = Closet.objects.update_or_create(closetid=myclosetid, defaults={'closetid':myclosetid})
	if(created):
		null_closet(myclosetid)

	imgurls =[]
	brands = []
	names = []

	#FIRST ADD TO OUTFIT RELATION
	outfitlen = Outfit.objects.count()
	myoutfitid = outfitlen
	Outfit.objects.create(outfitid=myoutfitid)
	#determine which pids belong to which parenttype 
	#		Closet.objects.filter(closetid=myclosetid).update(**{cname: addedproductid})
	for i in range(0, len(pids)):
		img = findprodattrib(pids[i], 'imgurl')
		imgurls.append(img)
		brand = findprodattrib(pids[i], 'brand')
		brands.append(brand)
		name = findprodattrib(pids[i], 'productname')
		names.append(name)

		mytype = findprodattrib(pids[i], 'producttype')
		myparent = findtypeattrib(mytype, 'parenttype')

		if(myparent == 'tops'):
			myparent = 'top'
		if(myparent== 'bottoms'):
			myparent = 'bottom'
		if(myparent == 'dresses'):
			myparent = 'dress'
		Outfit.objects.filter(outfitid=myoutfitid).update(**{myparent: pids[i]})
		added = addProductToCloset(pids[i], myclosetid)

		if(added == 0):
			print('closet is full')

	#ADD TO CLOSET RELATION
	#find the closet to put the outfit in
	colnum = 1
	cname = "outfit" + str(colnum)
	query =  Closet.objects.filter(closetid=myclosetid).values(cname)

	oid = query[0][cname]

	#look for an empty spot in THE CLOSET
	while oid is not 0 and oid is not None and colnum < 10:
		colnum += 1
		cname = "outfit" + str(colnum)
		query =  Closet.objects.filter(closetid=myclosetid).values(cname)

		if(query[0][cname] is not None):
			oid =int(query[0][cname]) 

	# at the end, either exited because no space, or found an empty space
	if oid is 0:
		#find an empty spot for the outfit to create an outfit id 
		Closet.objects.filter(closetid=myclosetid).update(**{cname: myoutfitid})
		result = [myclosetid, pids, imgurls, brands, names]
	else:
		print("closet is full, no more room for this outfit")
		result = ["closet is full, no more room for this outfit"]


	return render(request, 'add_outfit.html', {'results': result})


def generate_new_outfit(request):
	return render(request, 'generate_new_outfit.html', {})


def generateNewOutfit(request):
	print("do i get inside generate??")
	result = ['createrandomoutfit']
	return render(request, 'generate_new_outfit.html', {'results': result})

def viewOutfits(request):
	#TODO: change so that outfit:s and closets are separate??
	myclosetid =  request.GET.get('closetid')
	closetlist = Closet.objects.filter(closetid=myclosetid).values_list() #list
	
	if(closetlist.exists()):
		closettuple = closetlist[0]

		outfits = []
		nums = []
		#all of these outfit lists will also be lists of lists .....
		oimgs =[]
		obrands = []
		onames = []
		result =[]

		for x in range(51, len(closettuple)):

			if(closettuple[x] is not None and closettuple[x] != 0 and x > 50): #for every outfit
				#valid outfit ids 
				myimgs =[]
				mybrands = []
				mynames = []

				oid = closettuple[x]
				#list of outfit ids
				outfits.append(oid) 
				#using outfit id, get the individual products and then find all of their pids
				topid = findoutfitprod(oid, 'top')
				bottomid = findoutfitprod(oid, 'bottom')
				dressid = findoutfitprod(oid, 'dress')
				outerwearid = findoutfitprod(oid, 'outerwear')
				shoesid = findoutfitprod(oid, 'shoes')
				opids = [topid, bottomid, dressid, outerwearid, shoesid]
				#grab stuff for each outfit 
				for prod in opids:
					if prod is not None:
						imgurl = findprodattrib(prod, 'imgurl')
						brand = findprodattrib(prod, 'brand')
						name = findprodattrib(prod, 'productname')
						myimgs.append(imgurl)
						mybrands.append(brand)
						mynames.append(name)
				
				num = len(myimgs)
				print("appending this num to the array??" + str(num))

				nums.append(num)
				oimgs.append(myimgs)
				obrands.append(mybrands)
				onames.append(mynames)

		print("view closet, pieces in outfit!!")
		print(nums)
		#result[7-9] is for an outfits associated imgs brands and names 
		result = [myclosetid, outfits, nums, oimgs, obrands, onames]

	else:
		result = [myclosetid]

	return render(request, 'view_outfits.html', {'results': result})

def viewCloset(request):
	myclosetid = request.GET.get('closetid')
	closetlist = Closet.objects.filter(closetid=myclosetid).values_list() #list
	
	if(closetlist.exists()):
		closettuple = closetlist[0]


		imgurls = []
		names = []
		brands = []
		pids = []
		outfits = []
		nums = []
		#all of these outfit lists will also be lists of lists .....
		oimgs =[]
		obrands = []
		onames = []
		result =[]

		for x in range(1, len(closettuple)):
			# product id 
			if(closettuple[x] is not None and closettuple[x] != 0 and x < 51):
				image_query = Product.objects.filter(productid=closettuple[x]).values('imgurl')
				imgurl = image_query[0]['imgurl']
				name_query = Product.objects.filter(productid=closettuple[x]).values('productname')
				name = name_query[0]['productname']
				brand_query = Product.objects.filter(productid=closettuple[x]).values('brand')
				brand = brand_query[0]['brand']
				pid_query = Product.objects.filter(productid=closettuple[x]).values('productid')
				pid = pid_query[0]['productid']

				imgurls.append(imgurl)
				names.append(name)
				brands.append(brand)
				pids.append(pid)

			if(closettuple[x] is not None and closettuple[x] != 0 and x > 50): #for every outfit
				#valid outfit ids 
				myimgs =[]
				mybrands = []
				mynames = []

				oid = closettuple[x]
				#list of outfit ids
				outfits.append(oid) 
				#using outfit id, get the individual products and then find all of their pids
				topid = findoutfitprod(oid, 'top')
				bottomid = findoutfitprod(oid, 'bottom')
				dressid = findoutfitprod(oid, 'dress')
				outerwearid = findoutfitprod(oid, 'outerwear')
				shoesid = findoutfitprod(oid, 'shoes')
				opids = [topid, bottomid, dressid, outerwearid, shoesid]
				#grab stuff for each outfit 
				for prod in opids:
					if prod is not None:
						imgurl = findprodattrib(prod, 'imgurl')
						brand = findprodattrib(prod, 'brand')
						name = findprodattrib(prod, 'productname')
						myimgs.append(imgurl)
						mybrands.append(brand)
						mynames.append(name)
				
				num = len(myimgs)
				print("appending this num to the array??" + str(num))

				nums.append(num)
				oimgs.append(myimgs)
				obrands.append(mybrands)
				onames.append(mynames)

		print("view closet, pieces in outfit!!")
		print(nums)
		#result[7-9] is for an outfits associated imgs brands and names 
		result = [myclosetid, imgurls, names, brands, pids, outfits, nums, oimgs, obrands, onames]

	else:
		result = [myclosetid]

	return render(request, 'view_closet.html', {"results": result})
def null_closet(mycloset):
	for i in range(1,51):
		cname = "product" + str(i)
		Closet.objects.filter(closetid=mycloset).update(**{cname: 0})
	
	for j in range(1,11):
		cname = "outfit" + str(j)
		Closet.objects.filter(closetid=mycloset).update(**{cname: 0})
