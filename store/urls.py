from django.urls import path 
from . import views
urlpatterns = [
    path('', views.home , name="home"),
    path('shop', views.shop , name="shop"),
    path('update_item/', views.updateItem, name="update_item"),
    path('logout_user', views.logout_user , name="logout" ),
    path('checkout/', views.checkout, name="checkout"),
    path('getvar/', views.getvar, name="getvar"),
    path('search/',views.searchProduct, name='search'),
    path('searchc/',views.searchProductByCat, name='searchc'),







]