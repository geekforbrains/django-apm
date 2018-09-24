import time
from django.http import HttpResponse


def fast(request):
    return HttpResponse('fast request')


def slow(request):
    time.sleep(1.0)
    return HttpResponse('slow request')
