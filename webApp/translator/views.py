from django.http import HttpRequest, JsonResponse
from django.shortcuts import render
from translate import Translator
from django.http import JsonResponse, HttpResponse


def translate(request: HttpRequest):

    return render(request, 'translator.html')


def translate_text(request: HttpRequest):
    context = {}

    if 'input' in request.GET and request.GET['input']:
        translator = Translator(to_lang="tr")  # set language to Turkish

        # in case of error with translator, return empty data
        try:
            translation = translator.translate(request.GET['input'])
        except:
            return render(request, 'translator.html', context=context)

        context = {
            'input': request.GET['input'],
            'output': translation
        }
        return JsonResponse(context)

    return JsonResponse({})
