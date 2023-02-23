from django.urls import path
from . import views
app_name = 'customer_app'
urlpatterns = [
    path('cus_home',views.cus_home,name='customer_home'),
    path('my_cart',views.my_cart,name=''),
    path('my_orders',views.my_orders,name=''),
    path('view_product',views.view_product,name=''),
    path('logout',views.logout,name='logout'),
    path('edit_profile',views.edit_profile,name='edit_profile')
]