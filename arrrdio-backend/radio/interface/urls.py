from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("request", views.add, name="request"),
    path("resume", views.resume, name="resume")
]