from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'index.html')


def menu(request):
    return render(request, 'menu.html')

def list(request):
    return render(request, 'list.html')

def regist(request):
    return render(request, 'regist.html')


def user_page(request, user_name):
    return HttpResponse(f'<h1>{user_name}\'s page</h1>')