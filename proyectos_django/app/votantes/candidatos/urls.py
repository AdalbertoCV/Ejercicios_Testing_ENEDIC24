from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('Votar/<int:id>', views.votar, name='votarCandidato'),
]