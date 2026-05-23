from django.contrib import admin
from django.urls import path, include

from api.admin.blog.views import BlogListAPIView

urlpatterns = [
    path('list/', BlogListAPIView.as_view())
    # path('detail/<int:pk>/',include('api.admin.urls')),
]
