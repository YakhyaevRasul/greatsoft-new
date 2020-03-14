from django.urls import path
from .views import ContactToAPIView, ContactUsAPIView

urlpatterns = [
    path('us/', ContactUsAPIView.as_view()),
    path('to/', ContactToAPIView.as_view()),
]