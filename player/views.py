from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def test(request):
    return HttpResponse('<h3>This is a test if our program works. Wow!! it works</h3>')