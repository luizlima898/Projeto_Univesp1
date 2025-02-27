from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Olá, este é o meu primeiro app Django")
