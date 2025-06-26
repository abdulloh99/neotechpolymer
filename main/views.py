from django.shortcuts import render, redirect, HttpResponseRedirect
from .models import *
from django.db.models import Count
import random
from django.shortcuts import get_object_or_404

def base(request):
    kontakt = Contact.objects.first()

    context = {
        'Contact': kontakt,
    }
   
    return render(request, "base.html",context)

def index(request):
    slide = Slider.objects.all()
    shdesc = shortdesc.objects.first()
    product6 = Product.objects.all().order_by('-id')[3:6]
    homiy = hamkor.objects.all()
    kontakt = Contact.objects.first()
    yangilik3 = Yangiliklar.objects.all().order_by('-id')[0:3]

    
    context = {
        "Slider" : slide,
        "shortdesc" : shdesc,
        "Product" : product6,
        "hamkor" : homiy,
        'Contact': kontakt,
        'Yangiliklar': yangilik3,

    }
    
    return render(request, 'index.html',context)

def about(request):
    homiy = hamkor.objects.all()
    haqida = aboutus.objects.first()
    kontakt = Contact.objects.first()


    context = {
        "hamkor": homiy,
        "aboutus": haqida,
        'Contact': kontakt,

    }
    return render(request, "about.html",context)

def contact(request):
    kontakt = Contact.objects.first()

    context = {
        "Contact": kontakt,
    }
   
    return render(request, "contact.html",context)

def product(request):
    kontakt = Contact.objects.first()
    product = Product.objects.all()
    
    context = {
        'Product' : product,
        'kontakt' : kontakt,

    }
   
    return render(request, "products.html",context)

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    other_products = Product.objects.exclude(id=product.id)
    product4 = random.sample(list(other_products), min(4, other_products.count()))
    kontakt = Contact.objects.first()


    context = {
        'Product': product,
        'Product4': product4,
        "Contact": kontakt,

    }
    return render(request, "product-detail.html", context)

def blog(request):
    news = Yangiliklar.objects.all()
    kontakt = Contact.objects.first()


    context = {
        'yangilik' : news,
        'kontakt' : kontakt,
    }
   
    return render(request, "blog.html",context)

def blog_detail(request, slug):
    news = get_object_or_404(Yangiliklar, slug=slug)
    kontakt = Contact.objects.first()


    context = {
        'yangilik' : news,
        'Contact': kontakt,
    }
   
    return render(request, "blog-details.html",context)