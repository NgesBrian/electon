from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

def index(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'voting/index.html')
def signup(request):
    return render(request, 'voting/signup.html')
def login(request):
    return render(request, 'voting/login.html')
def about(request):
    return render(request, 'voting/about.html')
def contact(request):
    return render(request, 'voting/contact.html')