from django.contrib import admin
from django.urls import path
from .views import *
from django.http import HttpResponse, JsonResponse


urlpatterns = [
    path('', index),
]
