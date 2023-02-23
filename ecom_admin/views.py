from django.shortcuts import render,redirect
from common_app.models import Seller,Customer
from ecom_admin.models import Ecom_Admin
from django.http import HttpResponse
from django.conf import settings


# Create your views here.

def admin_home(request):
    return render(request,'ecom_admin/admin_home.html')

def seller_approval(request):
    return render(request,'ecom_admin/seller_approval.html')

def view_seller(request):
    seller_details = Seller.objects.all()
    return render(request,'ecom_admin/view_seller.html',{'sel_details':seller_details})

def view_customer(request):
    return render(request,'ecom_admin/view_customer.html')

def admin_login(request):
    msg =""
    if request.method == 'POST':
        admin_username = request.POST['a_username']
        admin_password = request.POST['a_password']
        try:
            admin_data = Ecom_Admin.objects.get(username = admin_username, password = admin_password)
            request.session['admin'] = admin_data.id
            return redirect('ecom_admin:admin_home')
        except:
            msg = 'invalid username or password'

    return render(request,'ecom_admin/admin_login.html',{'message':msg})

# def logout(request):
#     del request.session['admin']
#     request.session.flush()
#     return redirect('ecom_admin:admin_login')