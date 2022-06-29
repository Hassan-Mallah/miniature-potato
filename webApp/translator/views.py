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

    text2 = '''
    <!DOCTYPE html>
    
    <html>
    <head>
        <meta name="viewport" content="width=device-width"/>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.2/jquery.min.js">
        </script>
        <script type="text/javascript">
            $(document).ready(function () {
    
             $('#ajaxBtn').click(function(){
                $.ajax('/translator/ajax_data',   // request url
                {
                    success: function (data, status, xhr) {    // success callback function
                        $(document).ready(function () {
                            alert('Loading');
                        });

                            $('p').append(data);
                    }
                });
             });
    
            });
    
        </script>
    </head>
    <body>
    <h1> jQuery ajax() demo
    </h1>
    <input type="button" id="ajaxBtn" value="Send Ajax request"/>
    <p>
    </p>
    </body>
    </html>
    '''
    return HttpResponse(text2)


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


def ajax_data(request: HttpRequest):
    return HttpResponse('This is ajax data<br>')
