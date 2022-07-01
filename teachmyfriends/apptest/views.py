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
  fr.name = request.POST['name']
  fr.sex = request.POST['sex']
  fr.detail = request.POST['detail']
  fr.save()
  return redirect('/showlistfr')
  
def deletefr(request):
  id = request.POST['id']
  fr = friends.objects.get(id=id)
  fr.delete()
  return redirect('/showlistfr')


def updatefrshow(request):
  id = request.POST['id']
  fr = friends.objects.get(id=id)
  return render(request,'updatefr.html',{
    'fr':fr
  })
  

def updatefr(request):
  id = request.POST['id']
  fr = friends.objects.get(id=id)
  fr.name = request.POST['name']
  fr.sex = request.POST['sex']
  fr.detail = request.POST['detail']
  fr.save()
  return redirect('/showlistfr')
