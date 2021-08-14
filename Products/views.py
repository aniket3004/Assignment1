from django.shortcuts import render
from . models import Products

def ProductsView(request):
    products = Products.objects.all()
    context = {'products':products}
    return render(request,"Products/product.html",context)

