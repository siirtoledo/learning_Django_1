from django.shortcuts import render
from django.http import HttpResponse
from .models import Members


# Create your views here.
def member(request):
    members_data= Members.objects.all()
    print(members_data.values())
    con={"members_data":members_data}
    return render(request,"members.html",con)
    # return HttpResponse("<h1> Hello World</h1>")

def home(request):
    members_data= Members.objects.all()
    return render(request,"home.html",{"members_data":members_data})

def temp(request):
    return render(request,"home.html")

def details(request,id):
    single_member_data= Members.objects.filter(pk=id)
    print(single_member_data.values())
    return render(request,"details.html",{"single_member_data":single_member_data})