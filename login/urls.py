from django.urls import path
from login import views


urlpatterns = [
    path('login', views.index),
    path('register', views.register)
]
