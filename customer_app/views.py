from django.shortcuts import render, redirect
from common_app.models import Customer,Seller 
from seller.models import Products       #import class Customer
# from django.core.mail import send_mail
from django.conf import settings
from .decorators import auth_customer


# Create your views here.
def cus_home(request):
    customer_details = Customer.objects.get(id = request.session['customer'])
    return render(request,'customer/cus_home.html',{'cus_dtls':customer_details})

def view_product(request):
    product_list = Products.objects.all()
    return render(request,'customer/view_product.html',{'list_of_products':product_list})
@auth_customer
def my_cart(request):
    cart_data = Customer.objects.get(id = request.session['customer'])

    return render(request,'customer/my_cart.html')

def my_orders(request):
    return render(request,'customer/my_orders.html')

def logout(request):
    del request.session['customer']
    request.session.flush()
    return redirect('common_app:project_home')

def edit_profile(request):
    if request.method == 'POST':
        edt_name = request.POST['editprofile_name']
        edt_address = request.POST['editprofile_address']
        edt_mobile = request.POST['editprofile_mobile']
        edt_email = request.POST['editprofile_email']
        edt_gender = request.POST['editprofile_gender']

        # editcustomer = Customer(
        #     customer_name = edt_name,
        #     address = edt_address,
        #     mobile = edt_mobile,
        #     email = edt_email,
        #     gender = edt_gender
        # )
        updt = Customer.objects.filter(id = request.session['customer']).update(customer_name = edt_name,
            address = edt_address,
            mobile = edt_mobile,
            email = edt_email,
            gender = edt_gender)
        # editcustomer.save(id = request.session['customer'])
    return render(request,'customer/edit_profile.html')