from django.shortcuts import render,redirect
from . models import*
from django.contrib import messages

# Create your views here.
def contact(request ):
    return render(request,'contact.html')