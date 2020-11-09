from django.shortcuts import render, redirect
from django.contrib.postgres.search import SearchVector, SearchQuery
from .models import Hospitals, Donors

import ssl
import requests
from smtplib import SMTP
from . import config 

# Create your views here.


def index(request):
    if request.method == 'POST':
        query = SearchQuery(request.POST.get('query'))
        vector = SearchVector('hospitalName') + SearchVector('hospitalAddress')
        documents = Hospitals.objects.annotate(search=vector).filter(search=query)
        return render(request, "home/index.html", {
            "results": documents,
            "method": 'post'
        })
    return render(request, "home/index.html")


def selfassesment(request):
    if request.method == 'POST':
        return render(request, "home/self-assesment1.html", {
            "method": 'post'
        })
    return render(request, "home/self-assesment1.html")


def contact(request):
    return render(request, "home/contact-us.html")


def register(request):
    return render(request, "home/register.html")


def submissions(request):
    if request.method == 'POST':
        Donor = Donors.objects.create(
            donorName=request.POST.get('name'),
            donorMobile=request.POST.get('phone'),
            donorAge=request.POST.get('age'),
            donorAddress=request.POST.get('address'),
            donorCity=request.POST.get('city'),
            donorBloodgroup=request.POST.get('blood'),
            donorSex=request.POST.get('sex'),
            donorCovidrecord=request.POST.get('covid'),
            donorScreening=request.POST.get('date'),
            donorStatus=request.POST.get('plasma'),

        )
        Donor.save()
        return render(request, "home/donors.html", {
            'Donors': Donors.objects.all()
        })  


def donor(request):
    return render(request, "home/donorform.html")
