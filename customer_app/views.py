from django.shortcuts import render, redirect
from common_app.models import Customer,Seller 
from seller.models import Products       #import class Customer
# from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def cus_home(request):
    customer_details = Customer.objects.get(id = request.session['customer'])
    return render(request,'customer/cus_home.html',{'cus_dtls':customer_details})

def view_product(request):
    product_list = Products.objects.all()
    return render(request,'customer/view_product.html',{'list_of_products':product_list})

def my_cart(request):
    return render(request,'customer/my_cart.html')

def my_orders(request):
    return render(request,'customer/my_orders.html')

def logout(request):
    del request.session['customer']
    request.session.flush()
    return redirect('common_app:project_home')