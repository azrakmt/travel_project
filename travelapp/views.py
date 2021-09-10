# from django.http import HttpResponse
from django.shortcuts import render
from .models import place, travel


#Create your views here.
def fun(request):
    obj=place.objects.all()
    tour = travel.objects.all()
    return render(request,"index.html",{'results':obj,'recives': tour})

def add(request):
    num1=int(request.GET["num1"])
    num2=int(request.GET["num2"])
    num3=num1+num2

    return render(request,"result.html",{"add":num3})
