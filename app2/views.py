from django.shortcuts import render
from django.http import HttpResponse

# Create your views he
def bujji(request):
    return HttpResponse('this is bujji view')


def sowmya(request):
    return HttpResponse('this is sowmya view')