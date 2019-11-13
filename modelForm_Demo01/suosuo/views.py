import os

from django.http import HttpResponse
from django.shortcuts import render
# from suosuo import forms
# Create your views here.
from suosuo import forms


def suosuo(request):
    print("shiwei_home==", os.getenv("SHIWEI_HOME"))
    return HttpResponse("ok")

def book(request):
    if request.method == "GET":
        formData =  forms.BookForms()
    else:
        formData = forms.BookForms(request.POST)
        if formData.is_valid():
            print(formData.cleaned_data)
            return HttpResponse("is  book")


    return render(request, 'suosuo/book_html.html', {"form": formData})
