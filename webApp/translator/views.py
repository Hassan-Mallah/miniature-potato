from django.http import HttpResponse, HttpRequest
from django.template import loader


# Create your views here.

def index(request: HttpRequest):
    print(request.GET)
    print(request.POST)
    if 'text' in request.GET:
        print(request.GET['text'])

    template = loader.get_template('dictionary.html')

    # return HttpResponse('welcome to dictionary app')
    return HttpResponse(template.render())


def translate(request: HttpRequest):
    print('this is translate')

    return HttpResponse('response')
