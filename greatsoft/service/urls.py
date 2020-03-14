from django.urls import path
from .views import ServiceCreateAPIView, ServiceRetrieveUpdateDestroyAPIView, ServiceListAPIView

urlpatterns = [
    path('list/', ServiceListAPIView.as_view()),
    path('create/', ServiceCreateAPIView.as_view()),
    path('<int:pk>/', ServiceRetrieveUpdateDestroyAPIView.as_view()),
]