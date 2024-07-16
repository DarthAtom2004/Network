from django.contrib import admin
from django.urls import path
from MainNetworkApp import views
urlpatterns = [
    path('', views.FirstMessage),
    path('libraryGame', views.GameLibrary),
    path('libraryGame/<slug:slug>', views.GamePage)
]
