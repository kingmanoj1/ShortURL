
from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('code_generate/',code_generator,name="code_generator"),  
    path('appurl/<str:code>',redirecturl,name="redirecturl"), 
    path('Dashboard/',Dashboard,name="Dashboard"), 
     
]
