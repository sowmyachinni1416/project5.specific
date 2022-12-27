from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first(request):
    return HttpResponse('This is first view')

def chinni(request):
    return HttpResponse('this is chinni view')