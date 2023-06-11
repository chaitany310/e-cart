from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
path('', views.index,name = "shop"),
path('about/', views.about,name = "shop"),
path('contact/', views.contact,name = "shop"),
path('tracker/', views.tracker,name = "shop"),
path('search/', views.search,name = "shop"),
path('products/<int:myid>', views.prodView,name = "shop"),
path('checkout/', views.checkout,name = "shop"),
path('cart/', views.cart,name = "cart"),

]