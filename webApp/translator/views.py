from django.http import HttpRequest
from django.shortcuts import render
from translate import Translator
from django.http import HttpResponseRedirect
from .forms import NameForm
from django.contrib.auth.models import User
from django.http import JsonResponse

from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView


class SignUpView(CreateView):
    template_name = 'signup.html'
    form_class = UserCreationForm


def validate_username(request):
    print('validate_username')
    username = request.GET.get('username', None)
    data = {
        'is_taken': User.objects.filter(username__iexact=username).exists()
    }
    return JsonResponse(data)


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


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})
