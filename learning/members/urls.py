from django.urls import path
from . import views

urlpatterns =[
    path("",views.home, name="home"),
    path("member/",views.member, name="member"),
    path("view/",views.temp, name="view"),
    path("member/details/<str:id>",views.details, name="details")
    
    ]