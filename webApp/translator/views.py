from django.http import HttpRequest
from django.shortcuts import render
from translate import Translator
from django.http import JsonResponse, HttpResponse


def ajax(request):
    text = '''
    <!DOCTYPE html>
    <html>
    <head>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js">
        </script>
        <script>
            window.onload = function () {
                alert('window loaded');
            };
    
            $(document).ready(function () {
                alert('document loaded');
            });
        </script>
    </head>
    <body>
        <h1>Demo: window.onload() vs $(document).ready()</h1>
    </body>
    </html>
    '''
    return HttpResponse(text)


def translate(request: HttpRequest):
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

    return render(request, 'translator.html', context=context)
