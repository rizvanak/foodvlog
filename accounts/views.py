from django.shortcuts import render
from shop.models import *
from .models import *
# Create your views here.
def login(request):
    return render(request,'login.html')