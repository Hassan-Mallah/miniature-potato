from django.contrib import admin
from django.urls import path
from .views import *


urlpatterns = [
    path('get_name', get_name),
    path('signup', SignUpView.as_view()),
    path('', translate),
    path('validate_username/$', validate_username),

]
