from django.contrib import auth
from django.http import request, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # print(username)
        # print(password)

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            if 'next' in request.POST.keys():
                return HttpResponseRedirect(request.POST['next'])
            else:
                return HttpResponseRedirect(reverse('tables:index'))
        else:
            print('Пользователь не найден')
            userAuthRes = 'NoUser'
    else:
        print('Запрос не POST')
        userAuthRes = ''
    context = {
        'userAuthRes': userAuthRes
    }
    return render(request, 'authapp/login.html', context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('tables:index'))


def profile(request):
    # return render(request, 'authapp/login.html', context)
    return HttpResponseRedirect(reverse('tables:index'))
