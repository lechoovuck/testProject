from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('logproc/', log_proc, name='logproc'),
]
