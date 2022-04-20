from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'advertisement/home.html')

def about(request):
    return render(request, 'advertisement/.html')