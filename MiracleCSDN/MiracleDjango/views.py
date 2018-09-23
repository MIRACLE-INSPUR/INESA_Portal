
# Create your views here.
# -*- coding: utf-8 -*-
from django.shortcuts import render


def registered(request):
    return render(request, "registered.html")
