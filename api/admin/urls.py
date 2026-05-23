from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('blog/',include('api.admin.blog.urls')),
    path('common/',include('api.admin.common.urls')),
    # path('testing/',include('api.testing.urls')),
]
