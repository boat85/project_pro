from django.urls import path
from . import views

urlpatterns = [
 path('', views.showindex),
 path('addfriends', views.addfriends),
 path('showlistfr', views.showlistfr),
 path('insertfriend', views.insertfriend),
 path('deletefr', views.deletefr),
 path('updatefr', views.updatefr),
 path('updatefrshow', views.updatefrshow)
 
]
