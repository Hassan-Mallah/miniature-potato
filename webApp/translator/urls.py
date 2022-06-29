from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('ajax', ajax),
    path('ajax_data', ajax_data),
    path('', translate),
]
