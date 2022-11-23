from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def first_view(request):
    return HttpResponse("<h2 style='color:purple'>yay!let's start the work</h2>")
