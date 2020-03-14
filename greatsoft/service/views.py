from rest_framework import generics
from .models import Service
from .serializers import ServiceDetailSerializer, ServiceListSerializer
from rest_framework.permissions import IsAdminUser, AllowAny

class ServiceListAPIView(generics.ListAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceListSerializer
    permission_classes = [AllowAny, ]



class ServiceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Service.objects.all()
    serializer_class  = ServiceDetailSerializer
    permission_classes = [IsAdminUser,] 


class ServiceCreateAPIView(generics.CreateAPIView):
    queryset  = Service.objects.all()
    serializer_class  = ServiceDetailSerializer
    permission_classes = [IsAdminUser,]
