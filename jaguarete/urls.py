from django.urls import path

from . import views

app_name="jaguarete"

urlpatterns = [
    path('', views.index, name='index'),
    path('category/<str:categoria>', views.categoria, name='category'),
    path('product/<str:product>', views.product, name='product'),
    path('search/', views.search, name='search'),
]