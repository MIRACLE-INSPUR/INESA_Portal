
# Create your views here.
# -*- coding: utf-8 -*-
from django.shortcuts import render
from MiracleDjango import models


def registered(request):
    if request.method == "POST":
        email = request.POST.get("email", None)
        password = request.POST.get("password", None)
        country = request.POST.get("country", None)
        localLastName = request.POST.get("localLastName", None)
        localFirstName = request.POST.get("localFirstName", None)
        firstName = request.POST.get("firstName", None)
        lastName = request.POST.get("lastName", None)
        jobTitle = request.POST.get("jobTitle", None)
        workPhone = request.POST.get("workPhone", None)
        companyName = request.POST.get("companyName", None)
        address1 = request.POST.get("address1", None)
        address2 = request.POST.get("address2", None)
        city = request.POST.get("city", None)
        state = request.POST.get("state", None)
        postalCode = request.POST.get("postalCode", None)

        models.USER.objects.all(
            USER_email=email,
            USER_password=password,
            USER_country=country,
            USER_localLastName=localFirstName,
            USER_localFirstName=localLastName,
            USER_firstName=firstName,
            USER_lastName=lastName,
            USER_jobTitle=jobTitle,
            USER_workPhone=workPhone,
            USER_companyName=companyName,
            USER_address1=address1,
            USER_address2=address2,
            USER_city=city,
            USER_state=state,
            USER_postalCode=postalCode
        )
        user_list = models.USER.objects.all()
    return render(request, "registered.html")


def index(request):
    return render(request, "registered.html", {"data", registered()})
