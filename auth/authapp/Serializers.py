from rest_framework import serializers
from .models import *
class ProjectManagerSerializer(serializers.ModelSerializer):
    class Meta: 
        model = UserData
        fields = ('name', 'password')