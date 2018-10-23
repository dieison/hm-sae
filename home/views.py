from django.shortcuts import render, redirect
from django.contrib.auth import logout

def home(request):
    value1 = 10
    value2 = 20
    result = value1 * value2
    return render(request, 'home.html', {'result': result})


def my_logout(request):
    logout(request)
    return redirect('home')
