from dataclasses import field
from rest_framework import serializers
from .models import book


class TaskSerializer(serializers.ModelSerializer):
  
    class Meta:
        model = book
        fields = ('id','name','price')

# class TaskSerializer(serializers.ModelSerializer):
  
#     class Meta:
#         model = book
#         fields = ('id','name','price')