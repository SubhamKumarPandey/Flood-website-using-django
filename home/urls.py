from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index,name='home'),
    path("home1",views.home1,name='home1'),
    path("weather",views.weather,name='weather'),
    path("about",views.about,name='about'),
    path("contact",views.contact,name='contact'),
    path("location",views.location,name='location'),
    path("issue",views.issue,name='issue'),
    path("help",views.help,name='help'),
    path("reliefcamp",views.reliefcamp,name='reliefcamp'),
    path("rivers",views.rivers,name='rivers'),
    path("donation",views.donation,name='donation'),
    path("data",views.data,name='data'),
    path("data1",views.data1,name='data1'),
    path("data2",views.data2,name='data2'),
    path("data3",views.data3,name='data3'),
    path("data4",views.data4,name='data4'),
    path("register",views.register,name='register'),
    path("login",views.login,name='login'),
    path("logout",views.logout,name='logout')
    
    



]

