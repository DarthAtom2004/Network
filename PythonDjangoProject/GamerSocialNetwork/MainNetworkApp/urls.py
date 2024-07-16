from django.contrib import admin
from django.urls import path
from MainNetworkApp import views
urlpatterns = [
    path('', views.FirstMessage)
]
