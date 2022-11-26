from django.urls import path
from index import  views

urlpatterns = [
    path("home", views.index, name="index"),
]