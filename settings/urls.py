from django.urls import path
from settings import views

urlpatterns = [
    path('test', views.index),
]
