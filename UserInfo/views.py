from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect, reverse


# Create your views here.
def login(request):
    return render(request, 'login.html')