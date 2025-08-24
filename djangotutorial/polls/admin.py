from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]

from django.contrib import admin

from .models import Question

admin.site.register(Question)