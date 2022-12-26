from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'index.html')

def signup(request):

    if request.method == "POST":
        username = request.POST['username'];
        password = request.POST['password'];
        username = request.POST['username'];
        password2 = request.POST['password2'];
    else:
        return render(request, 'signup.html')