from django.urls import path

from . import views

app_name="jaguarete"

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<str:categoria>', views.categoria, name='category'),
    path('product/<str:product>', views.product, name='product'),
    path('search/', views.search, name='search'),
    path('add_to_cart/<str:product>', views.add_to_cart, name='add_to_cart'),
    path('del_cart_item/<str:product>', views.del_cart_item, name='del_cart_item'),
    path('add_product/', views.add_product, name='add_product'),
    path('carrito/', views.cart_list, name='cart_list'),
    path('del_product/<str:product>', views.del_product, name='del_product'),
    path('edit_product/<str:product>', views.edit_product, name='edit_product'),
    path('clear_cart/', views.clear_cart, name='clear_cart'),
    path('about/', views.about, name='about')
]