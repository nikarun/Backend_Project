from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import *
import requests as req
def Login(request):
    error=None
    if request.method == "POST":
        dict=request.POST
        username=dict["username"]
        password=dict["passwsord"]
        usr=authenticate(username=username,password=password)
        if usr != None:
            return redirect("enter_url")
        error="Wrong Username and Password"

    return render(request,"login.html",{"error":error})

def Enter_url(request):
    dict={}
    data=None
    if request.method=="POST":
        url=request.POST["url"]
        data=req.get(url)
        dict["data"]=data.text
        return render(request,"show_data.html",dict)


    return render(request,"enter_url.html",dict)