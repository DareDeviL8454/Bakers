from django.contrib import admin
from django.urls import path
from App import views
urlpatterns = [
    path('', views.index, name='inedex'),
    path('services', views.services, name='services'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('Button_basic', views.button_basic, name='Button_basic'),
    path('search', views.search, name="search"),
    path('menu', views.menu, name="menu"),
    path('cart',views.cart,name='cart'),
    path('checkout', views.checkout),
    path('final', views.final),
    path('Checkkout1', views.Checkout1),

]

