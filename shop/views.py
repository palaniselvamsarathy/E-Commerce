from django.shortcuts import render,redirect
from shop.models import Category,Products
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request,'shop/index.html')


def register(request):
    return render(request,'shop/register.html')


def collections(request):
    category = Category.objects.filter(status=0)
    return render(request,'shop/collections.html',{"category":category})

def collectionsview(request,name):
    if(Category.objects.filter(name=name,status=0)):
        products= Products.objects.filter(category__name=name)
        return render(request,'shop/products/index.html',{"products":products,"category":name})
    
    else:
        messages.warning(request,"No such Category Found")
        return redirect('collections')