from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    print("first dif is calling ")
    return render(request, "index.html")

