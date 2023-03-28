from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('logproc/', log_proc, name='logproc'),
    path('userprofile/', userprofile, name='userprofile'),
    # path('userprofile/password_edit/', password_edit, name='password_edit'),
]
