from timeit import repeat
from django.shortcuts import render
from .models import friends
# Create your views here.


def showindex(request):
  f = friends.objects.all()
  return render(request,'index.html',{'f':f})


