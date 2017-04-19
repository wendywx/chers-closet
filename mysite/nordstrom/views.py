from django.shortcuts import render
from django.http import HttpResponse

from .models import Product, Closet

def home(request):
	return render(request, 'home.html', {})

def browse_products(request):
	return render(request, 'browse_products.html', {})

def product_results(request):
	return render(request, 'product_results.html', {})

def added_to_closet(request):
	return render(request, "added_to_closet.html", {})

def addToCloset(request):
	addedproductid = request.GET.get('newproductid')
	myclosetid = request.GET.get('closetid')
	mycloset, created = Closet.objects.update_or_create(closetid=myclosetid, defaults={'closetid':myclosetid})
	null_closet(mycloset)
	colnum = 1
	cname = "product" + str(colnum)
	query =  Closet.objects.filter(closetid=myclosetid).values(cname)
	pid =int(query[0][cname]) 
	
	while pid is not 0 and pid < 50:
		colnum += 1
		cname = "product" + str(colnum)
		query =  Closet.objects.filter(closetid=myclosetid).values(cname)
		pid =int(query[0][cname]) 
	if pid is 0:
		Closet.objects.filter(closetid=myclosetid).update(**{cname: addedproductid})
		closet_query=Closet.objects.filter(closetid=myclosetid).values(cname)	

		#return the product name and imgurl to the html
		result = [addedproductid, myclosetid, closet_query[0][cname]]
	else:
		print("closet is full")
		result = ["closet is full"]

	#have to loop through every single product...

	return render(request, "added_to_closet.html", {"results": result})

def filterProducts(request):
	typeList = request.GET.getlist('types[]')

	result = []	
	productids = []
	images = []
	prices = []
	brands = []
	for i in typeList:
		productname_query = Product.objects.filter(producttype=i) #list
		pid_query = Product.objects.filter(producttype=i).values('productid')
		image_query = Product.objects.filter(producttype=i).values('imgurl') #list ...
		price_query = Product.objects.filter(producttype=i).values('price') #list 
		brand_query = Product.objects.filter(producttype=i).values('brand') #list 
		for j in range(0,len(image_query)):
			productids.append(pid_query[j]['productid'])
			images.append(image_query[j]['imgurl'])
			prices.append(price_query[j]['price'])
			brands.append(brand_query[j]['brand'])

		result = [productname_query, images, prices, brands, productids]

	return render(request, "product_results.html", {"results": result})

def about(request):
	return render(request, 'about.html', {})

def acct_home(request):
	return render(request, 'acct_home.html', {})

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
	return render(request, 'view_closet.html', {})

def null_closet(mycloset):
	mycloset.product1 = 0
	mycloset.product2 = 0
	mycloset.product3 = 0
	mycloset.product4 = 0
	mycloset.product5 = 0
	mycloset.product6 = 0
	mycloset.product7 = 0
	mycloset.product8 = 0
	mycloset.product9 = 0
	mycloset.product10 = 0
	mycloset.product11 = 0
	mycloset.product12 = 0
	mycloset.product13 = 0
	mycloset.product14 = 0
	mycloset.product15 = 0
	mycloset.product16 = 0
	mycloset.product17 = 0
	mycloset.product18 = 0
	mycloset.product19 = 0
	mycloset.product20 = 0
	mycloset.product21 = 0
	mycloset.product22 = 0
	mycloset.product23 = 0
	mycloset.product24 = 0
	mycloset.product25 = 0
	mycloset.product26 = 0
	mycloset.product27 = 0
	mycloset.product28 = 0
	mycloset.product29 = 0	
	mycloset.product30 = 0
	mycloset.product31 = 0
	mycloset.product32 = 0
	mycloset.product33 = 0
	mycloset.product34 = 0
	mycloset.product35 = 0
	mycloset.product36 = 0
	mycloset.product37 = 0
	mycloset.product38 = 0
	mycloset.product39 = 0
	mycloset.product40 = 0
	mycloset.product41 = 0
	mycloset.product42 = 0
	mycloset.product43 = 0
	mycloset.product44 = 0
	mycloset.product45 = 0
	mycloset.product46 = 0
	mycloset.product47 = 0
	mycloset.product48 = 0
	mycloset.product49 = 0
	mycloset.product50 = 0	
