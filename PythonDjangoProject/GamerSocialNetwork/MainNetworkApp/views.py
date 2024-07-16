from django.shortcuts import render
from django.http import HttpResponse

def FirstMessage(request):
    return HttpResponse("Main Netwok Page")

def GameLibrary(request):
    return HttpResponse(f"Game Library page")
def GamePage(request, game_id):
    return HttpResponse(f"Game Library page <p> Game Number: {game_id}</p>")
