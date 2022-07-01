from django.shortcuts import render
from .serializers import TaskSerializer
from .models import book
from rest_framework import generics
# Create your views here.

class TaskList(generics.ListAPIView):
    queryset = book.objects.all()
    serializer_class = TaskSerializer