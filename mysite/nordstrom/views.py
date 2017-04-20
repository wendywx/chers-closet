from django.shortcuts import render
from django.http import HttpResponse

from .models import Product, Closet, Type

def home(request):
	return render(request, 'home.html', {})

def browse_products(request):
	
	result0 = Type.objects.all()
	result1 = Product.objects.order_by().values_list('brand', flat=True).distinct()
	
	result = [result0, result1]
	return render(request, 'browse_products.html', {"results": result})

def product_results(request):
	return render(request, 'product_results.html', {})

def added_to_closet(request):
	return render(request, "added_to_closet.html", {})

def createNewOutfit(request):
	addedproductid = request.GET.get('newproductid')
	
	name_query = Product.objects.filter(productid=addedproductid).values('productname')
	name = name_query[0]['productname']
	
	image_query = Product.objects.filter(productid=addedproductid).values('imgurl')
	imgurl = image_query[0]['imgurl']

	mygender_q = Product.objects.filter(productid=addedproductid).values('gender')
	mygender = mygender_q[0]['gender']

	myproducttype_q = Product.objects.filter(productid=addedproductid).values('producttype')
	myproducttype = myproducttype_q[0]['producttype']

	mybrand_q = Product.objects.filter(productid=addedproductid).values('brand')
	mybrand = mybrand_q[0]['brand']

	myparenttype_q = Type.objects.filter(typename=myproducttype).values('parenttype')
	myparenttype = myparenttype_q[0]['parenttype']
	
	myseason_q= Type.objects.filter(typename=myproducttype).values('season')
	myseason = myseason_q[0]['season']
	
	myoccasion_q= Type.objects.filter(typename=myproducttype).values('occasion')
	myoccasion= myoccasion_q[0]['occasion']

	
	#myoutfitid # loop through outfit db and find next available id 

	#result = [imgurls]
	result = [name, imgurl, mygender, myproducttype, myparenttype, myseason, myoccasion]
	return render(request, "create_new_outfit.html", {"results": result})


def addToCloset(request):
	addedproductid = request.GET.get('newproductid')
	myclosetid = request.GET.get('closetid')
	print(addedproductid)
	print(myclosetid)
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
		result = [name+ " to closet " +myclosetid, imgurl]
	else:
		print("closet is full")
		result = ["closet is full"]

	return render(request, "added_to_closet.html", {"results": result})

def filterProducts(request):
	typeList = request.GET.getlist('types[]')
	brandList = request.GET.getlist('brands[]')

	result = []	
	names = []
	productids = []
	images = []
	prices = []
	brands = []
	for i in typeList:
		productname_query = Product.objects.filter(producttype=i).values('productname') #list
		pid_query = Product.objects.filter(producttype=i).values('productid')
		image_query = Product.objects.filter(producttype=i).values('imgurl') #list ...
		price_query = Product.objects.filter(producttype=i).values('price') #list 
		brand_query = Product.objects.filter(producttype=i).values('brand') #list 
		for j in range(0,len(image_query)):
			names.append(productname_query[j]['productname'])
			productids.append(pid_query[j]['productid'])
			images.append(image_query[j]['imgurl'])
			prices.append(price_query[j]['price'])
			brands.append(brand_query[j]['brand'])

		#result = [productname_query, images, prices, brands, productids]

	for k in brandList:
		productname_query = Product.objects.filter(brand=k).values('productname') #list
		pid_query = Product.objects.filter(brand=k).values('productid')
		image_query = Product.objects.filter(brand=k).values('imgurl') #list ...
		price_query = Product.objects.filter(brand=k).values('price') #list 
		brand_query = Product.objects.filter(brand=k).values('brand') #list 
		for l in range(0,len(pid_query)):
			names.append(productname_query[l]['productname'])
			productids.append(pid_query[l]['productid'])
			images.append(image_query[l]['imgurl'])
			prices.append(price_query[l]['price'])
			brands.append(brand_query[l]['brand'])

	
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

def log_in(request):
	return render(request, 'log_in.html', {})

def my_account(request):
	return render(request, 'my_account.html', {})

def register(request):
	return render(request, 'register.html', {})

def view_closet(request):
	myclosetid = request.GET.get('closetid')
	closetlist = Closet.objects.filter(closetid=myclosetid).values_list() #list
	closettuple = closetlist[0]
	result =[]
	for x in range(1, len(closettuple)):
		if(closettuple[x] is not None and closettuple[x] is not 0):
			result.append(closettuple[x])

	return render(request, 'view_closet.html', {"results": result})

def null_closet(mycloset):
	for i in range(1,50):
		cname = "product" + str(i)
		Closet.objects.filter(closetid=mycloset).update(**{cname: 0})
