from timeit import repeat
from django.shortcuts import render,redirect
from .models import friends
# Create your views here.


def showindex(request):
  return render(request,'index.html')

def showlistfr(request):
  f = friends.objects.all()
  return render(request,'showlistfriends.html',{'f':f})

def addfriends(request):
  return render(request,'addfriends.html')


def insertfriend(request):
  fr = friends()
  fr.name = request.GET['name']
  fr.sex = request.GET['sex']
  fr.detail = request.GET['detail']
  fr.save()
  return redirect('/showlistfr')
  