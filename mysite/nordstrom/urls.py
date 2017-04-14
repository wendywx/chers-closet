from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^home.html$', views.home, name = 'home'),
    url(r'^browse_products.html$', views.browse_products, name = 'browse_products'),
]