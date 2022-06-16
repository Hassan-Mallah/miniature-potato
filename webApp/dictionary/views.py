from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


# Create your views here.

def index(request):
    template = loader.get_template('dictionary.html')

    # return HttpResponse('welcome to dictionary app')
    return HttpResponse(template.render())
