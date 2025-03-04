from django.shortcuts import render, redirect

from mediamodels.models import Product, Category
from organiqueFood.models import ProductsFilter
from blog.models import BlogModels

from django.contrib.auth.decorators import login_required

from django.contrib import messages
from django.db.models import Q

from django.urls import  reverse
from django.http import HttpResponseRedirect

@login_required(login_url="user-login")
def index(request):
    filters = ProductsFilter.objects.all()
    products = Product.objects.all().order_by("-created")[0:8]
    categorys = Category.objects.all()
    blogs = BlogModels.objects.all()

    ctx = {
        'products': products,
        'categorys': categorys,
        'filters': filters,
        'blogs': blogs, 
    }
    return render(request, "organiqueFood/index.html", ctx)

def AllProducts(request):
    filters = ProductsFilter.objects.all()
    if request.method == "POST":
        searched = request.POST.get("searched") if request.POST.get("searched") else ''
        products = Product.objects.filter(
                Q(poster__username__icontains=searched) |
                Q(name__icontains=searched) |
                Q(price__icontains=searched) |
                Q(category__name__icontains=searched) |
                Q(filters__name__icontains=searched)
            ).order_by("created")
        searched_count = products.count()

        ctx = {
            "products": products,
            'searched': searched,
            'searched_count': searched_count,
            'filters': filters
        }
        if searched_count > 0:
            return render(request, "organiqueFood/all_products.html", ctx)
        else:
            return render(request, "organiqueFood/product_not_Found.html", ctx)
    products = Product.objects.all().order_by("discount")
    ctx = {
        "products": products
    }
    return render(request, "organiqueFood/all_products.html", ctx)

def ByCategory(request, pk):
    products = Product.objects.filter(
            Q(category__name__icontains=pk) |
            Q(filters__name__icontains=pk)
        ).order_by("created")

    ctx = {
        "products": products
    }

    return render(request, "organiqueFood/all_products.html", ctx)

def ProductViewer(request, pk):
    try:
        item = Product.objects.get(id=pk)
        ctx = {
            "item": item
        }
        return render(request, "organiqueFood/product.html", ctx)
    except:
        messages.error(request, "Product not Found")
    return render(request, "organiqueFood/product.html")
    

def AddItem(request, pk):
    product = Product.objects.get(id=pk)
    if request.user.is_authenticated:
        user = request.user
        if product.likes.filter(id=user.id).exists():
            product.likes.remove(user)
        else:
            product.likes.add(user)
        return HttpResponseRedirect(reverse("index"))

def AddToCart(request):
    pass