from django.urls import path
from .views import PhoneListCreateAPIView, PhoneRetrieveDestroyAPIView

urlpatterns = [
    path('phones/', PhoneListCreateAPIView.as_view()),
    path('phones/<int:pk>/', PhoneRetrieveDestroyAPIView.as_view())
]

