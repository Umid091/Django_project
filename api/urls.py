from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/',include('api.admin.urls')),
    # path('site/',include('api.site.urls')),
    # path('testing/',include('api.testing.urls')),
]
