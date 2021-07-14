from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth,User
from django.urls import reverse
from django.contrib.auth import login,logout
from django.contrib import messages
from .forms import ProductForm
from .models import Product
# Create your views here.

@login_required(login_url='sign_in')
def product_data(request):
    product_data = Product.objects.db_manager('Product_db').all()
    return render(request,"html/product_data.html",{"data":product_data})

@login_required(login_url='sign_in')
def product_create(request):
    if request.method == "GET":
        form = ProductForm
        return render(request,'html/product.html',{'form':form})
    else:
        form = ProductForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            weight = form.cleaned_data['weight']
            price = form.cleaned_data['price']
            data = Product(name=name,weight=weight,price=price)
            data.save()
            messages.success(request,"Product created Successfully !")
            return redirect('view_products')
        else:
            messages.error(request,"Invalid Data provided !")
            return redirect('product_create')

@login_required(login_url='sign_in')
def product_delete(request,pk):
    if request.method == "POST":
        data = Product.objects.db_manager('Product_db').get(pk=pk)
        data.delete()
        messages.success(request,"Product deleted Successfully !")
        return redirect('view_products')

@login_required(login_url='sign_in')
def product_update(request,pk):
    if request.method == 'POST':
        data = Product.objects.db_manager('Product_db').get(pk=pk)
        form = ProductForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
        messages.success(request,"Product updated Successfully !")
        return redirect('view_products')
    else:
        data = Product.objects.db_manager('Product_db').get(pk=pk)
        form = ProductForm(instance=data)
        return render(request,"html/product_update.html",{"form":form})

