import datetime
from django.shortcuts import render
from .models import Logging

def Logg(request):
    """
    from test main page.
    """
    ip = request.META.get('REMOTE_ADDR')
    referrer = request.META.get('HTTP_REFERER')
    time = datetime.datetime.now()
    request.META['HTTP_REFERER'] = '/example/uri/here/'
    return render(request, 'main.html', {'ip' : ip, 'referrer' : referrer, 'time' : time})

def Test1(request):
    """
    from test main page.
    """
    ip = request.META.get('REMOTE_ADDR')
    referrer = request.META.get('HTTP_REFERER')
    time = datetime.datetime.now()
    return render(request, 'page1.html', {'ip' : ip, 'referrer' : referrer, 'time' : time})

def Test2(request):
    """
    from test main page.
    """
    ip = request.META.get('REMOTE_ADDR')
    referrer = request.META.get('HTTP_REFERER')
    time = datetime.datetime.now()
    return render(request, 'page2.html', {'ip' : ip, 'referrer' : referrer, 'time' : time})

