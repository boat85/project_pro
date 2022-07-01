from django.urls import path
from . import views

urlpatterns = [
 path('', views.showindex),
 path('addfriends', views.addfriends)
]
