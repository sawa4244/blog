from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def test(request):
    return HttpResponse ("<h2>Главная{c}</h2>")

def main(request):
    return HttpResponse("<h1>Это мейн</h1>")
