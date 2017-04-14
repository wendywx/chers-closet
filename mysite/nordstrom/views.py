from django.shortcuts import render

def home(request):
	return render(request, 'home.html', {})

def browse_products(request):
	return render(request, 'browse_products.html', {})
