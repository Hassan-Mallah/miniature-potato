from django.shortcuts import render
from django.http import HttpRequest, HttpResponse


# Create your views here.

def news(request: HttpRequest):

    return HttpResponse('This is News App')
