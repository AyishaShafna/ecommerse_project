from django.urls import path
from . import views

urlpatterns = [
    path('admin_home',views.admin_home),
    path('seller_approval',views.seller_approval),
    path('view_seller',views.view_seller),
    path('view_customer',views.view_customer),
]