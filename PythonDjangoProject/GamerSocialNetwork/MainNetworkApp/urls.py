from django.contrib import admin
from django.urls import path, register_converter, re_path
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.FirstMessage, name='Home'),
    path('libraryGame', views.GameLibrary, name='GAYmLibrary'),
    path('libraryGame/<int:game_id>', views.GamePage, name='GAYmLibraryNumber'),
    path("gameyear/<year4:year>/", views.Archive, name='Archive')
]
