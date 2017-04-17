from django.shortcuts import render
from django.http import HttpResponse

from .models import Product

def home(request):
	return render(request, 'home.html', {})

def browse_products(request):
	return render(request, 'browse_products.html', {})

def product_results(request):
	return render(request, 'product_results.html', {})

def filterProducts(request):
	typeList = request.GET.getlist('types[]')

	result = []	
	for i in typeList:
		productname_query = Product.objects.filter(producttype=i) #list
		image_query = Product.objects.filter(producttype=i).values('imgurl').values() #list ...
		price_query = Product.objects.filter(producttype=i).values('price').values() #list 
		brand_query = Product.objects.filter(producttype=i).values('brand').values() #list 
		# for j in productname_query:
		# 	product = []
		# 	result.extend(j.values())
		result = [productname_query, image_query, price_query, brand_query]

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