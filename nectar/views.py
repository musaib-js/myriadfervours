from django.http import HttpResponse
from django.shortcuts import render

def index(request):
   return HttpResponse("Hello World");

def about(request):
   return HttpResponse("About Site");