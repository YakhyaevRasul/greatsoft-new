from rest_framework import generics
from .models import ContactTo, ContactUs
from .serializers import ContactToSerializer, ContactUsSerializer
from  rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated


class ContactToAPIView(generics.ListAPIView):
    queryset = ContactTo.objects.all()
    serializer_class = ContactToSerializer
    permission_classes = [IsAdminUser,]


class ContactUsAPIView(generics.ListAPIView):
    queryset = ContactUs.objects.all()
    serializer_class = ContactUsSerializer
    permission_classes = [IsAdminUser,]
