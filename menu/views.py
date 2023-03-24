from django.shortcuts import render

def index(request,**kwargs):
    return render(request, 'menu/layout.html')