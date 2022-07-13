from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('translate_text', translate_text),
    path('', translate),
]
