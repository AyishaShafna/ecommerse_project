from django.shortcuts import render, redirect
from common_app.models import Customer,Seller 
from seller.models import Products  
from customer_app.models import Cart     #import class Customer
# from django.core.mail import send_mail
from django.conf import settings
from .decorators import auth_customer
from django.db.models import F


# Create your views here.
def cus_home(request):
    customer_details = Customer.objects.get(id = request.session['customer'])
    return render(request,'customer/cus_home.html',{'cus_dtls':customer_details})



def view_product(request):
    product_list = Products.objects.all()
    return render(request,'customer/view_product.html',{'list_of_products':product_list})



@auth_customer
def my_cart(request):
   

    cart_data = Cart.objects.filter(customer_id = request.session['customer']).annotate(total = F('product__product_price')*F('qunatity'))
    grand_total = 0
    for i in cart_data:
        grand_total = i.total+grand_total
    request.session['grand'] = grand_total

    context = {'cart_item':cart_data,'grand_tot':grand_total}

    return render(request,'customer/my_cart.html',context)



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

    
        updt = Customer.objects.filter(id = request.session['customer']).update(customer_name = edt_name,
            address = edt_address,
            mobile = edt_mobile,
            email = edt_email,
            gender = edt_gender)
        # editcustomer.save(id = request.session['customer'])
    return render(request,'customer/edit_profile.html')

def product_details(request,pid):
    msg = ""
    prdct_dtls = Products.objects.get(id = pid)
    if request.method == 'POST':
        qntity = request.POST['qty']
        prod_exist = Cart.objects.filter(product_id = pid, customer_id = request.session['customer']).exists()
        if not prod_exist:
            item = Cart(
                qunatity = qntity,
                customer_id = request.session['customer'],
                product_id = pid
            )
            item.save()
        else:
            msg = 'item already exists'
    context = {'prdct_dtl':prdct_dtls,   #since we have to pass two variables prdct_dtls and msg, both of them store to another 
                'msg':msg                 #varirable named context and that context pass along url
    }
        

    return render(request,'customer/product_details.html',context)

def delete_cartitems(request,cart_id):
    delete_item = Cart.objects.get(id = cart_id)
    delete_item.delete()
    cart_data = Cart.objects.filter(customer_id = request.session['customer'])

    cart_data = Cart.objects.annotate(total = F('product__product_price')*F('qunatity'))
    return render(request,'customer/my_cart.html',{'cart_item':cart_data})

    


