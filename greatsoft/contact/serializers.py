from rest_framework import serializers
from .models import ContactUs, ContactTo


class ContactToSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactTo
        fields = ('id', 'info', 'date')


class ContactUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactUs
        fields = ('id', 'name', 'email', 'message')

        