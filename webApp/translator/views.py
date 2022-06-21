from django.http import HttpRequest
from django.shortcuts import render


# Create your views here.

def translate(request: HttpRequest):
    print(request.GET)
    print(request.POST)
    if 'text' in request.GET:
        print(request.GET['text'])

    context = {
        'input': 'test input',
        'output': 'test output'
    }
    return render(request, 'translator.html', context=context)
