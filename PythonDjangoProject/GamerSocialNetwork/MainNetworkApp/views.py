from django.shortcuts import render
from django.http import HttpResponse

def FirstMessage(request):
    return HttpResponse("Main Netwok Page")

def GameLibrary(request):
    return HttpResponse("Game Library page")
def GamePage(request, slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"Game Library page <p> Game Number: {slug}</p>")

def page_not_found(request, exception):
    return HttpResponse("Пошел на хуй сука")

