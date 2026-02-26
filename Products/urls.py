from django.urls import path
from Products import views

urlpatterns = [
    
    path('', views.home),
    path('Apple Mackbook/', views.Apple_Mackbook),
    path('HP Laptop/', views.hp_laptop),
    path('Dell Laptop/', views.dell_laptop),
    path('Lenovo Laptop/', views.lenovo_laptop),
    path('Asus Laptop/', views.asus_laptop)
    
    ]
