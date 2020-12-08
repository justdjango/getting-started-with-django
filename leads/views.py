from django.shortcuts import render
from django.http import HttpResponse


def home_page(request):
    # return HttpResponse("Hello world")
    return render(request, "second_page.html")