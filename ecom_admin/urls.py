from django.urls import path
from . import views
app_name = 'ecom_admin'

urlpatterns = [
    path('admin_home',views.admin_home,name='admin_home'),
    path('seller_approval',views.seller_approval),
    path('view_seller',views.view_seller),
    path('view_customer',views.view_customer),
    path('admin_login',views.admin_login),
    # path('logout',views.logout,name='logout')

]