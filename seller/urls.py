from django.urls import path
from . import views
app_name = 'seller'
urlpatterns = [
    path('sel_home',views.sel_home,name='sel_home'),
    path('add_product',views.add_product),
    path('update_stock',views.update_stock),
    path('change_pass',views.change_pass),
    path('order_his',views.order_his),
    path('prdct_cat',views.prdct_cat),
    path('recent_orders',views.recent_orders),
    path('sel_profile',views.sel_profile),
   
]