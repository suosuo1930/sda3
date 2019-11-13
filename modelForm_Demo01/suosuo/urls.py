from django.urls import path

from suosuo import views

urlpatterns = [
    path('book', views.book, name="book"),

]