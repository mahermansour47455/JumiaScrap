from django.urls import path
from . import views

urlpatterns = [
  path('home',views.ListeSmartphonesJumia,name='home'),
  path('search',views.search,name='search'),
]