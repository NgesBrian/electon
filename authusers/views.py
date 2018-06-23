from django.http import HttpResponse
from django.shortcuts import render, redirect

def home(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'authusers/home.html')
def dashboard(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'authusers/home.html')

def elections(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'authusers/home.html')

def results(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'authusers/home.html')