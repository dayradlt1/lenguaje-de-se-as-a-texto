from django.shortcuts import render
from django.http.response import HttpResponse
import joblib
# Create your views here.

def home(request):
    return render(request,'home.html',{})

def sistema(request):
    return render(request, 'Sistema.html',{})

def camara(request):
    cls: joblib.load('app.py')
    return render(request,"Sistema.html",{'cls':cls})
