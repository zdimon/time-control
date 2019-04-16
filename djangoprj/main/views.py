from django.shortcuts import render

# Create your views here.

from .models import WUsers

def home_page(request):
    users = WUsers.objects.all()
    return render(request,'main.html',{'users': users})