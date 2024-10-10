from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('settings/', include('settings.urls')),
    path('login/', include('login.urls')),
    path('main/', include('main.urls')),
]
