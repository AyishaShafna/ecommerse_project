from django.shortcuts import render, redirect
from common_app.models import Customer,Seller 
from seller.models import Products       #import class Customer
from django.core.mail import send_mail
from django.conf import settings

import random


 

# Create your views here.
def project_home(request):
    return render(request,'common_app/project_home.html')

def customerlogin(request):
    msg=""
    if request.method == 'POST':
        if 'c_signup' in request.POST:
            cust_name = request.POST['c_name']                    # here we are taking values from input fields to variable
            cust_address = request.POST['c_address']
            cust_mobile = request.POST['c_mobile']
            cust_email = request.POST['c_email']
            cust_gender = request.POST['c_gender']
            cust_password = request.POST['c_password']
            cust_confirmpassword = request.POST['c_confirmpassword']
            cust_image = request.FILES['c_image']


            cust1 = Customer(
                customer_name = cust_name,    # here we are storing these values(stored to variables in above steps) to the table creted by class in models.py
                address = cust_address,
                mobile = cust_mobile,
                email = cust_email,
                gender = cust_gender,
                password = cust_password,
                confirm_password = cust_confirmpassword,
                image = cust_image
                )
            cust1.save()

        if 'c_login' in request.POST:

            cust_login_username = request.POST['login_username']
            cust_login_password = request.POST['login_password']
            try:
                customer = Customer.objects.get(email = cust_login_username, password = cust_login_password)
                request.session['customer'] = customer.id
                return redirect('customer_app:customer_home')
            except:
                msg = 'invalid email id or password'
        
    return render(request,'common_app/customerlogin.html',{'msg':msg})

    # return render(request,'common_app/customerlogin.html')



def sellerlogin(request):
    msg = ""
    sel = ""
    if request.method == 'POST':
        if 's_signup' in request.POST:

            sel_name = request.POST['s_company_name']
            seller_company_address = request.POST['s_company_address']
            seller_company_mobile = request.POST['s_mobile']
            seller_company_email = request.POST['s_email']
            seller_company_logo = request.FILES['s_company_logo']
            seller_bank_name = request.POST['s_bank_name']
            seller_acc_holder = request.POST['s_acc_holdername']
            seller_acc_no = request.POST['s_acc_no']
            seller_ifsc = request.POST['s_ifsc']
            sel_username=random.randint(1111,9999)
            sel_password= 'sel-' + sel_name.lower()+ str(sel_username)
            message = 'hai your user name is ' + str(sel_username)+'and password is' + sel_password
        
            seller1 = Seller(
                company_name = sel_name,
                company_address = seller_company_address,
                company_mobile = seller_company_mobile,
                company_email = seller_company_email,
                company_logo = seller_company_logo,
                bank_name = seller_bank_name,
                acc_holder =  seller_acc_holder,
                acc_no = seller_acc_no,
                ifsc_code =  seller_ifsc,
                seller_username = sel_username,
                seller_password = sel_password
                )
            
            send_mail(
                'username and temporry password ',
                message,
                settings.EMAIL_HOST_USER,
                [seller_company_email],
                fail_silently = False
                )
            seller1.save()
        # return render(request,'common_app/sellerlogin.html')

        if 's_login' in request.POST:
            sel_login_username = request.POST['seller_username']
            sel_login_password = request.POST['seller_password']
            try:
                seller = Seller.objects.get(seller_username = sel_login_username, seller_password = sel_login_password)
                request.session['seller'] = seller.id
                # sel = Seller.objects.filter(seller_username = sel_login_username, seller_password = sel_login_password).values(company_name)
                return redirect('seller:sel_home')
            except:
                msg = 'invalid email id or password'
    return render(request,'common_app/sellerlogin.html',{'msg':msg})


def admin_login(request):
    return render(request,'common_app/admin_login.html')