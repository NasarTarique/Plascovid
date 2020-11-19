from django.db import models
from django.urls import reverse

# Create your models here.

sex = [
    ('M', "Male"),
    ('F', "Female"),
    ('O', "Others")
]

status = [
    ("Y", "Yes"),
    ("N", "No")
]

bloodgroup = [
    ("A+", "A+"),
    ("A-", "A-"),
    ("AB+", "AB+"),
    ("AB-", "AB-"),
    ("B+", "B+"),
    ("B-", "B-"),
    ("O+", "O+"),
    ("O-", "O-")
]

class Hospitals(models.Model):
    hospitalName = models.TextField(max_length=300)
    hospitalAddress = models.TextField(max_length=400)
    hospitalContact = models.TextField(max_length=200)

    def __str__(self):
        return f"{self.hospitalName}"


class Donors(models.Model):
    donorName = models.CharField(max_length=50)
    donorMobile = models.CharField(max_length=15)
    donorMail = models.CharField(max_length=30)
    donorAge = models.IntegerField()
    donorAddress = models.TextField(max_length=150)
    donorCity = models.CharField(max_length=30)
    donorBloodgroup = models.CharField(max_length=3, choices=bloodgroup)
    donorSex = models.CharField(max_length=1, choices=sex)
    donorCovidrecord = models.CharField(max_length=1, choices=status)
    donorScreening = models.DateField()


class Receivers(models.Model):
    receiverName = models.CharField(max_length=50)
    receiverAge = models.IntegerField()
    receiverHospital = models.TextField(max_length=200)
    receiverAddress = models.TextField(max_length=250)
    receiverCity = models.CharField(max_length=30)
    receiverBloodgroup = models.CharField(max_length=3, choices=bloodgroup)
    receiverCaretaker = models.CharField(max_length=50)
    receiverCaretakercontact = models.CharField(max_length=15)
    receiverCaretakeremail = models.CharField(max_length=30)
    receiverDocs = models.ImageField(upload_to = "media/")

    
    def get_absolute_url(self):
        return reverse('profile', args=[str(self.id)])
