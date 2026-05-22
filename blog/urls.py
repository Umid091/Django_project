from django.urls import path
from .views import PostListCreateApiview

urlpatterns = [
    path('posts/', PostListCreateApiview.as_view()),
]