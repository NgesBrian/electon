from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

def home(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'users/home.html')
def dashboard(request):
    return render(request, 'users/dashboard.html')

