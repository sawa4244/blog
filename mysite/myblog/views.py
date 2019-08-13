from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def test(request):
    return render (request, 'base.html', {})

def main(request):
    return HttpResponse("<h1>Это мейн</h1>")
