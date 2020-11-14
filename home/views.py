from django.shortcuts import render, redirect
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.contrib.auth.models import User
from .models import Hospitals, Donors, Receivers
from .mail import donormail, mail

from . import config 

# Create your views here.

# home page
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

# self assement page
def selfassesment(request):
    if request.method == 'POST':
        return render(request, "home/self-assesment1.html", {
            "method": 'post'
        })
    return render(request, "home/self-assesment1.html")

# contact page 
def contact(request):
    if request.method == 'POST':
        subject = f"Mail form plascovid user : {request.POST.get('name')}"
        body = f"\n{request.POST.get('content')}Email : {request.POST.get('mail')}\n\nPhone : {request.POST.get('phone')}"
        mail('nasartarique@gmail.com',subject, body)
        return render(request, "home/contact-us.html")
    return render(request, "home/contact-us.html")

# register for donor
def register(request):
    return render(request, "home/register.html", {
        'receivers': False
    })

# register as recievers 
def rregister(request):
    return render(request, "home/register.html", {
        'receivers':True
    })


def receiverform(request):
    if request.method == 'POST':
        return render(request, "home/info.html", {
            'receivers': True
        }) 
    return render(request, "home/receiverform.html")

# display donor form 
def donorform(request):
    return render(request, "home/donorform.html")
# after submissions of donor form
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
        return render(request, "home/donors.html")  

# submissions of receiver form 

def rsubmissions(request):
    if request.method == 'POST':
        Receiver = Receivers.objects.create(
            receiverName=request.POST.get('name'),
            receiverHospital=request.POST.get('hospital'),
            receiverAge=request.POST.get('age'),
            receiverAddress=request.POST.get('address'),
            receiverCity=request.POST.get('city'),
            receiverBloodgroup=request.POST.get('bloodgroup'),
            receiverCaretaker =request.POST.get('caretaker'),
            receiverCaretakercontact=request.POST.get('caretakernumber'),
            receiverCaretakeremail=request.POST.get('caretakermail'),
            receiverDocs=request.POST.get('hopsdata'),

        )
        Receiver.save()
        donormail(request.POST.get('city'), request.POST.get('bloodgroup'), Receiver.get_absolute_url())
        return render(request, "home/donors.html")  

# displaying donor data
def donorinfo(request):
    if request.method == 'POST':
        query = SearchQuery(request.POST.get('region')) & SearchQuery(request.POST.get('bloodgroup'))
        vector = SearchVector('donorAddress') + SearchVector('donorCity') + SearchVector('donorBloodgroup')
        documents = Donors.objects.annotate(rank=SearchRank(vector, query)).order_by('-rank').filter(donorBloodgroup=request.POST.get('bloodgroup'))
        return render(request, "home/info.html", {
            'receiving':False,
            'Donors':documents
        })
    return render(request, "home/info.html", {
        'receiving':False,
        'Donors': Donors.objects.all()
    })

#  displaying receiver info

def receiverinfo(request):
    if request.method == 'POST':
        query = SearchQuery(request.POST.get('region'))
        vector = SearchVector('receiverAddress') + SearchVector('receiverCity')
        documents = Receivers.objects.annotate(rank=SearchRank(vector, query)).order_by('-rank').filter(receiverBloodgroup=request.POST.get('bloodgroup'))
        return render(request, "home/info.html", {
            'receiving':True,
            'Receivers':documents
        })
    return render(request, "home/info.html", {
        'receiving':True,
        'Receivers': Receivers.objects.all()
    })

# Creation of account 
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


def profile(request, num):
    receiver = Receivers.objects.get(pk=num)
    return render(request, "home/profile.html",{
        'receiver': receiver
    })
    
