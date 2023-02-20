from django.shortcuts import render, redirect
from django.http import HttpResponse
from seller.models import Products #import class Customer
from common_app.models import Seller
# from django.core.mail import send_mail
from django.conf import settings

import random

# Create your views here.
def sel_home(request):
    seller_dt = Seller.objects.get(id = request.session['seller'])
    return render(request,'seller/sel_home.html',{'dt':seller_dt})

def add_product(request):

    if request.method == 'POST':
        pr_name = request.POST['p_name']
        pr_price = request.POST['p_price']
        pr_no = request.POST['p_number']
        pr_cat = request.POST['p_category']
        pr_desc = request.POST['p_description']
        pr_stock = request.POST['p_stock']
        pr_images = request.FILES['p_images']

        newproduct = Products(
            seller_id = request.session['seller'],
            product_name = pr_name,
            product_price = pr_price,
            product_no = pr_no,
            product_category = pr_cat,
            product_description = pr_desc,
            product_stock = pr_stock,
            product_images = pr_images
        )
        newproduct.save()
    return render(request,'seller/add_product.html')

def update_stock(request):
    return render(request,'seller/update_stock.html')

def change_pass(request):
    return render(request,'seller/change_pass.html')

def order_his(request):
    return render(request,'seller/order_his.html')

def prdct_cat(request):
    product_list = Products.objects.filter(seller_id = request.session['seller'])

    return render(request,'seller/prdct_cat.html',{'list':product_list})

def recent_orders(request):
    return render(request,'seller/update_stock.html')

def sel_profile(request):
    seller_dtls = Seller.objects.get(id = request.session['seller'])

    return render(request,'seller/sel_profile.html',{'dtls':seller_dtls})
