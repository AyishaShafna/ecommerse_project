from django.shortcuts import render,redirect

def auth_customer(func):
    def wrap(request,*args,**kwargs):
        if 'customer' in request.session:
            return func(request,*args,**kwargs)
        else:
            return redirect('common_app:project_home')
    return wrap