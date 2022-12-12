from django.shortcuts import render

from .models import IpRegister

def index(request):
    list_ip = IpRegister.objects.all()
    return render(request,'ipregister.html',{'list_ip':list_ip})
