from django.shortcuts import render, redirect
from django.http import HttpResponse


def FirstMessage(request):
    return HttpResponse("Main Netwok Page")


def GameLibrary(request):
<<<<<<< HEAD
    return HttpResponse(f"Game Library page")


def GamePage(request, game_id):
    return HttpResponse(f"Game Library page <p> Game Number: {game_id}</p>")


def Archive(request, year):
    if year > 2024:
        return redirect('Home')
=======
    return HttpResponse("Game Library page")
def GamePage(request, slug):
    if request.GET:
        print(request.GET)
    return HttpResponse(f"Game Library page <p> Game Number: {slug}</p>")

def page_not_found(request, exception):
    return HttpResponse("Пошел на хуй сука")

>>>>>>> 914d61577b9e6261f09688e3ddce116cc9cf222f
