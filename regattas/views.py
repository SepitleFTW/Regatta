from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello and welcome to beginning of regatta results!")