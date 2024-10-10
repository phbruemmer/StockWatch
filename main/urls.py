from django.urls import path
from main import views


urlpatterns = [
    path('test', views.index),
]
