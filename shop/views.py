from django.shortcuts import render,redirect
from shop.models import Category,Products
from django.contrib import messages
from django.http import JsonResponse


# Create your views here.
def home(request):
    products = Products.objects.filter(trending=1)
    return render(request,'shop/index.html',{"products":products})


def register(request):
    return render(request,'shop/register.html')


def collections(request):
    category = Category.objects.filter(status=0)
    return render(request,'shop/collections.html',{"category":category})

def collectionsview(request,name):
    if(Category.objects.filter(name=name,status=0)):
        products= Products.objects.filter(category__name=name)
        return render(request,'shop/products/index.html',{"products":products,"category_name":name})
    
    else:
        messages.warning(request,"No such Category Found")
        return redirect('collections')
    

def product_details(request,cname,pname):
    if(Category.objects.filter(name=cname,status=0)):
      if(Products.objects.filter(name=pname,status=0)):
        products=Products.objects.filter(name=pname,status=0).first()
        return render(request,"shop/products/product_details.html",{"products":products})
      else:
        messages.error(request,"No Such Prodtuct Found")
        return redirect('collections')
    else:
      messages.error(request,"No Such Catagory Found")
      return redirect('collections')