from django.urls import path
from login import views


urlpatterns = [
    path('test', views.index),
    path('register', views.register)
]
