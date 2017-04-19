from django.shortcuts import render
from django.http import HttpResponse

from .models import Product, Closet, Type

def home(request):
	return render(request, 'home.html', {})

def browse_products(request):
	result = Type.objects.all()
	return render(request, 'browse_products.html', {"results": result})

def product_results(request):
	return render(request, 'product_results.html', {})

def added_to_closet(request):
	return render(request, "added_to_closet.html", {})

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

	
	while pid is not 0 and colnum < 51:
		colnum += 1
		cname = "product" + str(colnum)
		query =  Closet.objects.filter(closetid=myclosetid).values(cname)
		pid =int(query[0][cname]) 

	if pid is 0:

		Closet.objects.filter(closetid=myclosetid).update(**{cname: addedproductid})

		closet_query=Closet.objects.filter(closetid=myclosetid).values(cname)	
		result = [addedproductid, myclosetid, closet_query[0][cname]]
	else:
		print("closet is full")
		result = ["closet is full"]

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
	for i in range(1,51):
		cname = "product" + str(i)
		Closet.objects.filter(closetid=mycloset).update(**{cname: 0})
