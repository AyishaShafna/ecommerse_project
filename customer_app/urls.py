from django.urls import path
from . import views
app_name = 'customer_app'
urlpatterns = [
    path('cus_home',views.cus_home,name='customer_home'),
    path('my_cart',views.my_cart,name='my_cart'),
    path('my_orders',views.my_orders,name='my_orders'),
    path('view_product',views.view_product,name='view_product'),
    path('logout',views.logout,name='logout'),
    path('edit_profile',views.edit_profile,name='edit_profile'),
    path('product_details/<int:pid>',views.product_details,name='product_details'),
    path('delete_cartitems/<int:cart_id>',views.delete_cartitems,name= 'delete_cartitems')
]