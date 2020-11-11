from django.db import models

# Create your models here.


class Hospitals(models.Model):
    hospitalName = models.TextField(max_length=300)
    hospitalAddress = models.TextField(max_length=400)
    hospitalContact = models.TextField(max_length=200)

    def __str__(self):
        return f"{self.hospitalName}"


class Donors(models.Model):

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

    donorName = models.CharField(max_length=50)
    donorMobile = models.CharField(max_length=15)
    donorAge = models.IntegerField()
    donorAddress = models.TextField(max_length=150)
    donorCity = models.CharField(max_length=30)
    donorBloodgroup = models.CharField(max_length=3, choices=bloodgroup)
    donorSex = models.CharField(max_length=1, choices=sex)
    donorCovidrecord = models.CharField(max_length=1, choices=status)
    donorScreening = models.DateField()
    donorStatus = models.CharField(max_length=1, choices=status)
