from django.shortcuts import render
from .serializers import TaskSerializer
from .models import book
from rest_framework import generics
from rest_framework import generics, permissions
# Create your views here.

class BookList(generics.ListAPIView):
    queryset = book.objects.all()
    serializer_class = TaskSerializer
    
    permission_classes = [permissions.IsAuthenticated]
    
    
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = book.objects.all()
    serializer_class = TaskSerializer
    
    