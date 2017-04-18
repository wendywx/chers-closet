from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.home, name = 'home'),
    url(r'^home.html$', views.home, name = 'home'),
    url(r'^browse_products.html$', views.browse_products, name = 'browse_products'),
    url(r'^filterProducts/$', views.filterProducts, name='filterProducts'),
    url(r'^product_results.html$', views.product_results, name = 'product_results'),
    url(r'^about.html$', views.about, name = 'about'),
    url(r'^acct_home.html$', views.acct_home, name = 'acct_home'),
    url(r'^contact.html$', views.contact, name = 'contact'),
    url(r'^create_new_closet.html$', views.create_new_closet, name = 'create_new_closet'),
    url(r'^create_new_outfit.html$', views.create_new_outfit, name = 'create_new_outfit'),
    url(r'^log_in.html$', views.log_in, name = 'log_in'),
    url(r'^my_account.html$', views.my_account, name = 'my_account'),
    url(r'^register.html$', views.register, name = 'register'),
    url(r'^view_closet.html$', views.view_closet, name = 'view_closet'),
    url(r'^addToCloset/$', views.addToCloset, name='addToCloset'),
    url(r'^added_to_closet.html$', views.added_to_closet, name = 'added_to_closet'),
]