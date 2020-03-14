from rest_framework  import serializers
from .models import Service


class ServiceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('name', 'image')



class ServiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'

