from django.urls import path
from . import views

app_name = 'common_app'

urlpatterns = [
    path('project_home',views.project_home,name='project_home'),
    path('customerlogin',views.customerlogin,name='login'),
    path('sellerlogin',views.sellerlogin),
    path('admin_login',views.admin_login),
]