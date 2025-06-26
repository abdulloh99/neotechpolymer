from django.urls import path
from .views import *

urlpatterns = [
    path('base/', base, name= "base"),
    path('', index, name= "index"),
    path('about', about, name= "about"),
    path('contact', contact, name= "contact"),
    path('product', product, name= "products"),
    path('blog', blog, name= "blog"),
    path('blog-details/<slug:slug>/', blog_detail, name= "blog-details"),
    path('product-detail/<slug:slug>/', product_detail, name= "product-detail"),
]