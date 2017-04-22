import random

from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Closet, Type

def home(request):
	return render(request, 'home.html', {})


def findprodattrib(productid, attribname):
	myattrib_q = Product.objects.filter(productid=productid).values(attribname)
	myattrib = myattrib_q[0][attribname]
	return myattrib


def findtypeattrib(mytypename, attribname):
	myattrib_q = Type.objects.filter(typename=mytypename).values(attribname)
	myattrib = myattrib_q[0][attribname]
	return myattrib


def generate_product(query, myseason, myoccasion):
	product = list(query.values_list(flat=True)) #generate random products
	if len(product) > 0:
		seasonflag = 0
		occasionflag = 0

		myproduct = 0

		while seasonflag != 1 or occasionflag != 1:
			seasonflag = 0
			occasionflag = 0

			rand_num = random.randint(0,len(product)-1)
			myproduct = product[rand_num]#pid
			producttype = findprodattrib(myproduct, 'producttype')
			productseason = findtypeattrib(producttype, 'season').split(':')
			productoccasion = findtypeattrib(producttype, 'occasion').split(':')

			for i in productseason:
				if i in myseason:
					seasonflag = 1

			for j in productoccasion:
				if j in myoccasion:
					occasionflag = 1

		productimgurl = findprodattrib(myproduct, 'imgurl')
		brand = findprodattrib(myproduct,'brand')
		name = findprodattrib(myproduct,'productname')
		return [productimgurl, brand, name]
	else:
		return [0]


def browse_products(request):
	junk = ["Shoe tree", "Polish", "Insoles", "Brush"]
	types = list(Type.objects.order_by('typename').all().values_list('typename', flat=True))
	for i in junk:
		types.remove(i)
	brands = Product.objects.order_by('brand').values_list('brand', flat=True).distinct()
	prices = ['$0-$50','$50-$100', '$100-$200', '$200-$400','$400-$1000']
	
	result = [types, brands, prices]
	return render(request, 'browse_products.html', {"results": result})


def product_results(request):
	return render(request, 'product_results.html', {})


def added_to_closet(request):
	return render(request, "added_to_closet.html", {})


def view_closet(request):
	return render(request, "view_closet.html", {})


def generateOutfit(mypid):
	#modify to return a list of imgurls, brands and names
	result = []
	imgurls = []
	brands = []
	names =[]

	tops = list(Type.objects.filter(parenttype="tops").values_list(flat=True))
	bottoms = list(Type.objects.filter(parenttype="bottoms").values_list(flat=True))
	outerwear = list(Type.objects.filter(parenttype="outerwear").values_list(flat=True))
	shoes = list(Type.objects.filter(parenttype="shoes").values_list(flat=True))
	dresses = list(Type.objects.filter(parenttype="dresses").values_list(flat=True))

	athletic = list(Type.objects.filter(occasion="athletic").values_list(flat=True))
	work = list(Type.objects.filter(occasion="work").values_list(flat=True))
	dressy = list(Type.objects.filter(occasion="dressy").values_list(flat=True))
	casual = list(Type.objects.filter(occasion="casual").values_list(flat=True))

	name = findprodattrib(mypid, 'productname')
	myimgurl = findprodattrib(mypid, 'imgurl')
	myproducttype = findprodattrib(mypid, 'producttype')
	mygender = findprodattrib(mypid, 'gender')
	myparenttype = findtypeattrib(myproducttype, 'parenttype')
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

		print('generate outerwear')
		generated_outerwear = generate_product(outerwear_q, myseason, myoccasion) #generate outerwear
		if len(generated_outerwear) > 1:
			imgurls.append(generated_outerwear[0])
			brands.append(generated_outerwear[1])
			names.append(generated_outerwear[2])

		topimgurl = findprodattrib(mypid,'imgurl') #user chosen top
		brand = findprodattrib(mypid,'brand')
		name = findprodattrib(mypid,'productname')
		imgurls.append(topimgurl)	
		brands.append(brand)
		names.append(name)

		generated_bottom = generate_product(bottoms_q, myseason, myoccasion) #generate bottom
		imgurls.append(generated_bottom[0])
		brands.append(generated_bottom[1])
		names.append(generated_bottom[2])

		generated_shoes = generate_product(shoes_q, myseason, myoccasion) #generate top
		imgurls.append(generated_shoes[0])
		brands.append(generated_shoes[1])
		names.append(generated_shoes[2])

	elif(myparenttype == "bottoms"): 

		generated_outerwear = generate_product(outerwear_q, myseason, myoccasion) #generate outerwear
		if len(generated_outerwear) > 1:
			imgurls.append(generated_outerwear[0])
			brands.append(generated_outerwear[1])
			names.append(generated_outerwear[2])

		generated_top = generate_product(tops_q, myseason, myoccasion) #generate top
		imgurls.append(generated_top[0])
		brands.append(generated_top[1])
		names.append(generated_top[2])

		bottomimgurl = findprodattrib(mypid,'imgurl') #user chosen bottom
		imgurls.append(bottomimgurl)
		brand = findprodattrib(mypid,'brand')
		name = findprodattrib(mypid,'productname')
		brands.append(brand)
		names.append(name)

		generated_shoes = generate_product(shoes_q, myseason, myoccasion) #generate shoes
		imgurls.append(generated_shoes[0])
		brands.append(generated_shoes[1])
		names.append(generated_shoes[2])

	elif(myparenttype == "outerwear"): 

		outerwearimgurl = findprodattrib(mypid,'imgurl') #user chosen outerwear
		imgurls.append(outerwearimgurl)
		brand = findprodattrib(mypid,'brand')
		name = findprodattrib(mypid,'productname')	
		brands.append(brand)
		names.append(name)

		if 'dressy' in myoccasion: #since dresses are categorized only as dressy
			if random.randint(0,1) == 0: #randomly choose whether to match outerwear with dress or with top/bottom
				
				generated_top = generate_product(tops_q, myseason, myoccasion)
				imgurls.append(generated_top[0])
				brands.append(generated_top[1])
				names.append(generated_top[2])

				generated_bottom = generate_product(bottoms_q, myseason, myoccasion)
				imgurls.append(generated_bottom[0])
				brands.append(generated_bottom[1])
				names.append(generated_bottom[2])

			else:
				generated_dress = generate_product(dresses_q, myseason, myoccasion)
				imgurls.append(generated_dress[0])
				brands.append(generated_dress[1])
				names.append(generated_dress[2])

		else: 
			generated_top = generate_product(tops_q, myseason, myoccasion)
			imgurls.append(generated_top[0])
			brands.append(generated_top[1])
			names.append(generated_top[2])

			generated_bottom = generate_product(bottoms_q, myseason, myoccasion)
			imgurls.append(generated_bottom[0])
			brands.append(generated_bottom[1])
			names.append(generated_bottom[2])

		generated_shoes = generate_product(shoes_q, myseason, myoccasion)
		imgurls.append(generated_shoes[0])
		brands.append(generated_shoes[1])
		names.append(generated_shoes[2])

	elif(myparenttype == "dresses"): 

		generated_outerwear = generate_product(outerwear_q, myseason, myoccasion) #generate outerwear
		if len(generated_outerwear) > 1:
			imgurls.append(generated_outerwear[0])
			brands.append(generated_outerwear[1])
			names.append(generated_outerwear[2])

		#user input dress
		dressimgurl = findprodattrib(mypid,'imgurl')
		imgurls.append(dressimgurl)
		brand = findprodattrib(mypid,'brand')
		name = findprodattrib(mypid,'productname')
		brands.append(brand)
		names.append(name)

		generated_shoes = generate_product(shoes_q, myseason, myoccasion)
		imgurls.append(generated_shoes[0])
		brands.append(generated_shoes[1])
		names.append(generated_shoes[2])

	elif(myparenttype == "shoes"):

		generated_outerwear = generate_product(outerwear_q, myseason, myoccasion)
		if len(generated_outerwear) > 1:
			imgurls.append(generated_outerwear[0])
			brands.append(generated_outerwear[1])
			names.append(generated_outerwear[2])

		dress = list(dresses_q.values_list(flat=True)) #generate random dress
		if 'dressy' in myoccasion:
			if random.randint(0,1) == 0: #randomly choose whether to match outerwear with dress or with top/bottom
				generated_top = generate_product(tops_q, myseason, myoccasion)
				imgurls.append(generated_top[0])
				brands.append(generated_top[1])
				names.append(generated_top[2])

				generated_bottom = generate_product(bottoms_q, myseason, myoccasion)
				imgurls.append(generated_bottom[0])
				brands.append(generated_bottom[1])
				names.append(generated_bottom[2])

			else:
				generated_dress = generate_product(dresses_q, myseason, myoccasion)
				imgurls.append(generated_dress[0])
				brands.append(generated_dress[1])
				names.append(generated_dress[2])

		else:	
			generated_top = generate_product(tops_q, myseason, myoccasion)
			imgurls.append(generated_top[0])
			brands.append(generated_top[1])
			names.append(generated_top[2])

			generated_bottom = generate_product(bottoms_q, myseason, myoccasion)
			imgurls.append(generated_bottom[0])
			brands.append(generated_bottom[1])
			names.append(generated_bottom[2])

		#user input shoes
		shoesimgurl = findprodattrib(mypid, 'imgurl')
		imgurls.append(shoesimgurl)
		brand = findprodattrib(mypid,'brand')
		name = findprodattrib(mypid,'productname')
		brands.append(brand)
		names.append(name)

	else:
		print("error: something is wrong with parenttype")

	result =[imgurls, brands, names]
	return result


def createMyOutfit(request):
	pidList = request.GET.getlist('pids[]')
	top = 0; 
	bottom = 0; 
	dress = 0; 
	outerwear = 0; 
	shoes = 0; 

	myclosetid = request.GET.get('closetid')
	print(myclosetid)

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

	imgurls = generateOutfit(addedproductid)

	result = imgurls
	result.append(addedproductid)
	return render(request, "create_new_outfit.html", {"results": result})


def addToCloset(request):
	addedproductid = request.GET.get('newproductid')
	myclosetid = request.GET.get('closetid')

	closet_query=Closet.objects.filter(closetid=myclosetid).values('product1')

	mycloset, created = Closet.objects.update_or_create(closetid=myclosetid, defaults={'closetid':myclosetid})
	if(created):
		null_closet(myclosetid)

	colnum = 1
	cname = "product" + str(colnum)
	query =  Closet.objects.filter(closetid=myclosetid).values(cname)

	pid =query[0][cname]

	
	while pid is not 0 and pid is not None and colnum < 50:
		colnum += 1
		cname = "product" + str(colnum)
		query =  Closet.objects.filter(closetid=myclosetid).values(cname)
		print(query)
		print(cname)
		if(query[0][cname] is not None):
			pid =int(query[0][cname]) 


	if pid is 0:
		Closet.objects.filter(closetid=myclosetid).update(**{cname: addedproductid})
		closet_query=Closet.objects.filter(closetid=myclosetid).values(cname)	
		name_query = Product.objects.filter(productid=addedproductid).values('productname')
		name = name_query[0]['productname']
		image_query = Product.objects.filter(productid=addedproductid).values('imgurl')
		imgurl = image_query[0]['imgurl']
		result = [name+ " to closet " + myclosetid, imgurl, myclosetid]
	else:
		print("closet is full")
		result = ["closet is full"]

	return render(request, "added_to_closet.html", {"results": result})

def filterProducts(request):
	type_list = request.GET.getlist('types[]')
	brand_list = request.GET.getlist('brands[]')
	price_list = request.GET.getlist('prices[]')
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

	if len(type_list) == 0:
		results_query = Product.objects.all()
	else:
		for i in type_list:
			types_query = Product.objects.filter(producttype=i)
			results_query = results_query | types_query

	if len(brand_list) == 0:
		results_query_1 = results_query
	else:
		for j in brand_list:
			brands_query = results_query.filter(brand=j)
			results_query_1 = results_query_1 | brands_query
	
		#results_query = results_query_1
	if len(price_list) == 0:
		results_query_2 = results_query_1
	else: 
		for k in reformatted_price_list:
			minimum = k[0]
			maximum = k[1]
			price_query = results_query_1.filter(price__range=(minimum,maximum))
			results_query_2 = results_query_2 | price_query

	results_query = results_query_2

	for product in results_query:
		names.append(product.productname)
		images.append(product.imgurl)
		prices.append(product.price)
		brands.append(product.brand)
		productids.append(product.productid)

	result = [names, images, prices, brands, productids]


	return render(request, "product_results.html", {"results": result})

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
	#if every outfit is filled, say closet is full
	result= [myclosetid]
	return render(request, 'add_outfit.html', {'results': result})


def generate_new_outfit(request):
	return render(request, 'generate_new_outfit.html', {})


def generateNewOutfit(request):
	print("do i get inside generate??")
	result = ['createrandomoutfit']
	return render(request, 'generate_new_outfit.html', {'results': result})


def viewCloset(request):
	myclosetid = request.GET.get('closetid')
	closetlist = Closet.objects.filter(closetid=myclosetid).values_list() #list
	closettuple = closetlist[0]
	print(closettuple)
	imgurls = []
	names = []
	brands = []
	pids = []
	result =[]

	for x in range(1, len(closettuple)):
		if(closettuple[x] is not None and closettuple[x] is not 0):
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

	print(pids)
	result = [imgurls, names, brands, pids, myclosetid]
	return render(request, 'view_closet.html', {"results": result})


def null_closet(mycloset):
	for i in range(1,51):
		cname = "product" + str(i)
		Closet.objects.filter(closetid=mycloset).update(**{cname: 0})

	for j in range(1,11):
		cname = "outfit" + str(j)
		Closet.objects.filter(closetid=mycloset).update(**{cname: 0})
