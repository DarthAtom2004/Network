from django.shortcuts import render
from django.http import HttpResponse

def FirstMessage(request):
    return HttpResponse("Main Netwok Page")
