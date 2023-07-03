from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home),
    path('login/', views.login),
    path('register/', views.register),
    path('black/', views.black),
    path('contacts/', views.contacts),
    path('designer/', views.designer),
    path('gallery/', views.gallery),
]