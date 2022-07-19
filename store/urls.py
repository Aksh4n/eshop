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
    path('contact/',views.contact, name='contact'),
    path('test/',views.test, name='test'),
    path('register/',views.register_user, name='register'),
    path('login/',views.login_user, name='login'),
    path('profile/',views.profile, name='profile'),
    path('about/',views.about, name='about'),
    path('updateprofile/',views.updateprofile, name='updateprofile'),












]