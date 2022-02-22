from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Monica Django Project<html><body><h1> Hello World Monica is doing Django now</body></html>")