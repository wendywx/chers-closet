import random

from django.shortcuts import render
from django.http import HttpResponse

from .models import Product, Closet, Type

def home(request):
	return render(request, 'home.html', {})

def browse_products(request):
	
	types = Type.objects.order_by('typename').all()
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
	result = []

	tops = list(Type.objects.filter(parenttype="tops").values_list(flat=True))
	bottoms = list(Type.objects.filter(parenttype="bottoms").values_list(flat=True))
	outerwear = list(Type.objects.filter(parenttype="outerwear").values_list(flat=True))
	shoes = list(Type.objects.filter(parenttype="shoes").values_list(flat=True))
	dresses = list(Type.objects.filter(parenttype="dresses").values_list(flat=True))

	athletic = list(Type.objects.filter(occasion="athletic").values_list(flat=True))
	work = list(Type.objects.filter(occasion="work").values_list(flat=True))
	dressy = list(Type.objects.filter(occasion="dressy").values_list(flat=True))
	casual = list(Type.objects.filter(occasion="casual").values_list(flat=True))

	name_query = Product.objects.filter(productid=mypid).values('productname')
	name = name_query[0]['productname']
	
	image_query = Product.objects.filter(productid=mypid).values('imgurl')
	myimgurl = image_query[0]['imgurl']

	myproducttype_q = Product.objects.filter(productid=mypid).values('producttype')
	myproducttype = myproducttype_q[0]['producttype']

	mygender_q = Product.objects.filter(productid=mypid).values('gender')
	myparenttype_q = Type.objects.filter(typename=myproducttype).values('parenttype')

	myseason_q= Type.objects.filter(typename=myproducttype).values('season')
	myoccasion_q= Type.objects.filter(typename=myproducttype).values('occasion')

	mygender = mygender_q[0]['gender']
	myparenttype = myparenttype_q[0]['parenttype']
	myseason = myseason_q[0]['season']
	myoccasion= myoccasion_q[0]['occasion']

	occasions=[athletic, casual, dressy, work]
	if(myoccasion == 'athletic'):
		myocc = 0
	elif(myoccasion == 'casual'):
		myocc = 1
	elif(myoccasion == 'dressy'):
		myocc=2
	elif(myoccasion == 'work'):
		myocc = 3
	else:
		print("something is wrong w occasion still tho")

	myproducts_q = Product.objects.filter(gender=mygender)

	# filter down to type
	tops_q = myproducts_q.filter(producttype__in=tops)
	bottoms_q = myproducts_q.filter(producttype__in=bottoms)
	dresses_q = myproducts_q.filter(producttype__in=dresses)
	shoes_q = myproducts_q.filter(producttype__in=shoes)
	outerwear_q = myproducts_q.filter(producttype__in=outerwear)

	#filter down by occasion
	tops_q = tops_q.filter(producttype__in=occasions[myocc])
	bottoms_q = bottoms_q.filter(producttype__in=occasions[myocc])	
	dresses_q = dresses_q.filter(producttype__in=occasions[myocc])
	shoes_q = shoes_q.filter(producttype__in=occasions[myocc])
	outerwear_q = outerwear_q.filter(producttype__in=occasions[myocc])


	# 5 possible parenttype choices, generate random parenttypes based on our already filtered queries
	if(myparenttype == "tops"): #need to generate outerwear, bottoms, shoes
		
		outerwear = list(outerwear_q.values_list(flat=True)) #generate random outerwear
		if len(outerwear) > 0:
			rand_num = random.randint(0,len(outerwear)-1)
			print(rand_num)
			myouterwear = outerwear[rand_num]#pid
			image_query = Product.objects.filter(productid=myouterwear).values('imgurl')
			outerwearimgurl = image_query[0]['imgurl']
			result.append(outerwearimgurl)

		image_query = Product.objects.filter(productid=mypid).values('imgurl') #user input top
		topimgurl = image_query[0]['imgurl']
		result.append(topimgurl)

		bottom = list(bottoms_q.values_list(flat=True)) #generate random bottoms
		rand_num = random.randint(0,len(bottom)-1)
		mybottom = bottom[rand_num]#pid
		image_query = Product.objects.filter(productid=mybottom).values('imgurl')
		bottomimgurl = image_query[0]['imgurl']
		result.append(bottomimgurl)

		shoes = list(shoes_q.values_list(flat=True)) #generate random shoes
		rand_num = random.randint(0,len(shoes)-1)
		myshoes = shoes[rand_num]#pid
		image_query = Product.objects.filter(productid=myshoes).values('imgurl')
		shoesimgurl = image_query[0]['imgurl']
		result.append(shoesimgurl)


	elif(myparenttype == "bottoms"): #need to generate outerwear, tops, shoes

		outerwear = list(outerwear_q.values_list(flat=True)) #generate random outerwear
		if len(outerwear) > 0:
			rand_num = random.randint(0,len(outerwear)-1)
			print(rand_num)
			myouterwear = outerwear[rand_num]#pid
			image_query = Product.objects.filter(productid=myouterwear).values('imgurl')
			outerwearimgurl = image_query[0]['imgurl']
			result.append(outerwearimgurl)

		top = list(tops_q.values_list(flat=True)) #generate random tops
		rand_num = random.randint(0,len(top)-1)
		mytop = top[rand_num]#pid
		image_query = Product.objects.filter(productid=mytop).values('imgurl')
		topimgurl = image_query[0]['imgurl']
		result.append(topimgurl)

		image_query = Product.objects.filter(productid=mypid).values('imgurl') #user input bottom
		bottomimgurl = image_query[0]['imgurl']
		result.append(bottomimgurl)

		shoes = list(shoes_q.values_list(flat=True)) #generate random shoes
		rand_num = random.randint(0,len(shoes)-1)
		myshoes = shoes[rand_num]#pid
		image_query = Product.objects.filter(productid=myshoes).values('imgurl')
		shoesimgurl = image_query[0]['imgurl']
		result.append(shoesimgurl)

	elif(myparenttype == "outerwear"): #need to generate either dress and shoes or set of tops, bottoms, shoes

		image_query = Product.objects.filter(productid=mypid).values('imgurl') #user input outerwear
		outerwearimgurl = image_query[0]['imgurl']
		result.append(outerwearimgurl)

		dress = list(dresses_q.values_list(flat=True)) #generate random dress
		if len(dress) > 0:

			if random.randint(0,1) == 0: #randomly choose whether to match outerwear with dress or with top/bottom

				top = list(tops_q.values_list(flat=True)) #generate random tops
				rand_num = random.randint(0,len(top)-1)
				mytop = top[rand_num]#pid
				image_query = Product.objects.filter(productid=mytop).values('imgurl')
				topimgurl = image_query[0]['imgurl']
				result.append(topimgurl)

				bottom = list(bottoms_q.values_list(flat=True)) #generate random bottoms
				rand_num = random.randint(0,len(bottom)-1)
				mybottom = bottom[rand_num]#pid
				image_query = Product.objects.filter(productid=mybottom).values('imgurl')
				bottomimgurl = image_query[0]['imgurl']
				result.append(bottomimgurl)

			else:

				rand_num = random.randint(0,len(dress)-1)
				mydress = dress[rand_num]#pid
				image_query = Product.objects.filter(productid=mydress).values('imgurl')
				dressimgurl = image_query[0]['imgurl']
				result.append(dressimgurl)

		else:
			top = list(tops_q.values_list(flat=True)) #generate random tops
			rand_num = random.randint(0,len(top)-1)
			mytop = top[rand_num]#pid
			image_query = Product.objects.filter(productid=mytop).values('imgurl')
			topimgurl = image_query[0]['imgurl']
			result.append(topimgurl)

			bottom = list(bottoms_q.values_list(flat=True)) #generate random bottoms
			rand_num = random.randint(0,len(bottom)-1)
			mybottom = bottom[rand_num]#pid
			image_query = Product.objects.filter(productid=mybottom).values('imgurl')
			bottomimgurl = image_query[0]['imgurl']
			result.append(bottomimgurl)

		shoes = list(shoes_q.values_list(flat=True)) #generate random shoes
		rand_num = random.randint(0,len(shoes)-1)
		myshoes = shoes[rand_num]#pid
		image_query = Product.objects.filter(productid=myshoes).values('imgurl')
		shoesimgurl = image_query[0]['imgurl']
		result.append(shoesimgurl)

	elif(myparenttype == "dresses"): #need to generate outerwear and shoes

		outerwear = list(outerwear_q.values_list(flat=True)) #generate random outerwear
		if len(outerwear) > 0:
			rand_num = random.randint(0,len(outerwear)-1)
			print(rand_num)
			myouterwear = outerwear[rand_num]#pid
			image_query = Product.objects.filter(productid=myouterwear).values('imgurl')
			outerwearimgurl = image_query[0]['imgurl']
			result.append(outerwearimgurl)

		image_query = Product.objects.filter(productid=mypid).values('imgurl') #user input outerwear
		dressimgurl = image_query[0]['imgurl']
		result.append(dressimgurl)

		shoes = list(shoes_q.values_list(flat=True)) #generate random shoes
		rand_num = random.randint(0,len(shoes)-1)
		myshoes = shoes[rand_num]#pid
		image_query = Product.objects.filter(productid=myshoes).values('imgurl')
		shoesimgurl = image_query[0]['imgurl']
		result.append(shoesimgurl)

	elif(myparenttype == "shoes"):

		outerwear = list(outerwear_q.values_list(flat=True)) #generate random outerwear
		if len(outerwear) > 0:
			rand_num = random.randint(0,len(outerwear)-1)
			print(rand_num)
			myouterwear = outerwear[rand_num]#pid
			image_query = Product.objects.filter(productid=myouterwear).values('imgurl')
			outerwearimgurl = image_query[0]['imgurl']
			result.append(outerwearimgurl)

		dress = list(dresses_q.values_list(flat=True)) #generate random dress
		if len(dress) > 0:

			if random.randint(0,1) == 0: #randomly choose whether to match outerwear with dress or with top/bottom

				top = list(tops_q.values_list(flat=True)) #generate random tops
				rand_num = random.randint(0,len(top)-1)
				mytop = top[rand_num]#pid
				image_query = Product.objects.filter(productid=mytop).values('imgurl')
				topimgurl = image_query[0]['imgurl']
				result.append(topimgurl)

				bottom = list(bottoms_q.values_list(flat=True)) #generate random bottoms
				rand_num = random.randint(0,len(bottom)-1)
				mybottom = bottom[rand_num]#pid
				image_query = Product.objects.filter(productid=mybottom).values('imgurl')
				bottomimgurl = image_query[0]['imgurl']
				result.append(bottomimgurl)

			else:

				rand_num = random.randint(0,len(dress)-1)
				mydress = dress[rand_num]#pid
				image_query = Product.objects.filter(productid=mydress).values('imgurl')
				dressimgurl = image_query[0]['imgurl']
				result.append(dressimgurl)

		else:
			
			top = list(tops_q.values_list(flat=True)) #generate random tops
			rand_num = random.randint(0,len(top)-1)
			mytop = top[rand_num]#pid
			image_query = Product.objects.filter(productid=mytop).values('imgurl')
			topimgurl = image_query[0]['imgurl']
			result.append(topimgurl)

			bottom = list(bottoms_q.values_list(flat=True)) #generate random bottoms
			rand_num = random.randint(0,len(bottom)-1)
			mybottom = bottom[rand_num]#pid
			image_query = Product.objects.filter(productid=mybottom).values('imgurl')
			bottomimgurl = image_query[0]['imgurl']
			result.append(bottomimgurl)

		image_query = Product.objects.filter(productid=mypid).values('imgurl') #user input outerwear
		shoesimgurl = image_query[0]['imgurl']
		result.append(shoesimgurl)

	else:
		print("error: something is wrong with parenttype")

	return result

def createMyOutfit(request):
	pidList = request.GET.getlist('pids[]')
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

	result = [imgurls]
	#result = [name, imgurl, mygender, myproducttype, myparenttype, myseason, myoccasion]
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

	#result = results_query
	#print(result)
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
	for i in range(1,50):
		cname = "product" + str(i)
		Closet.objects.filter(closetid=mycloset).update(**{cname: 0})
