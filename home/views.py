from django.shortcuts import render, redirect
from django.contrib.postgres.search import SearchVector, SearchQuery
from .models import Hospitals

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


def donor(request):
    return render(request, "home/donorform.html")
