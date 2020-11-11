from django.shortcuts import render, redirect
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.contrib.auth.models import User
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


def donorinfo(request):
    if request.method == 'POST':
        query = SearchQuery(request.POST.get('region')) & SearchQuery(request.POST.get('bloodgroup'))
        vector = SearchVector('donorAddress') + SearchVector('donorCity') + SearchVector('donorBloodgroup')
        documents = Donors.objects.annotate(rank=SearchRank(vector, query)).order_by('-rank')
        return render(request, "home/info.html", {
            'Donors':documents
        })
    return render(request, "home/info.html", {
        'Donors': Donors.objects.all()
    })


def userform(request):
    if request.method == 'POST':
        if User.objects.filter(username=request.POST.get('username')):
            return render(request, "home/userform.html",{
                'userexists': True,
                'username': request.POST.get('username')
            })
        user = User.objects.create_user(request.POST.get('username'), email=request.POST.get('email'), password=request.POST.get('password'))
        user.save()
    return render(request, "home/userform.html" ,{
        'userexists': False
    })
