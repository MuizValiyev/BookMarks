from django.urls import path, include
from .views import dashboard, register

urlpatterns = [
    path('', include('django.contrib.auth.urls')), 
    path('', dashboard, name='dashboard'),
    path('register/', register, name='register'),
]
