from django.contrib import admin
from django.urls import path, register_converter, re_path
from . import views
from . import converters

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
<<<<<<< HEAD
    path('', views.FirstMessage, name='Home'),
    path('libraryGame', views.GameLibrary, name='GAYmLibrary'),
    path('libraryGame/<int:game_id>', views.GamePage, name='GAYmLibraryNumber'),
    path("gameyear/<year4:year>/", views.Archive, name='Archive')
=======
    path('', views.FirstMessage),
    path('libraryGame', views.GameLibrary),
    path('libraryGame/<slug:slug>', views.GamePage)
>>>>>>> 914d61577b9e6261f09688e3ddce116cc9cf222f
]
