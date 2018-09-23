
# Create your views here.
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    #request.POST
    #request.GET
    #return  HttpResponse("hello lujihao!!!!!!")
    return  render(request,"index.html")