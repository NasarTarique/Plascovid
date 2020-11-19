from .models import Donors
import os
# from .config import EMAIL_ADDRESS, EMAIL_PWD, TEST_MAIL
from smtplib import SMTP

import ssl
import requests


def mail(mail, subject, body):
    context = ssl.create_default_context()
    with SMTP("smtp.gmail.com") as smtp:
        smtp.ehlo()
        smtp.starttls(context=context)
        smtp.ehlo()
        Subject = subject
        Body = body
        msg = f"Subject:{Subject}\n\n{Body}"
        EMAIL_ADDRESS = os.environ.get('EMAIL')
        EMAIL_PWD = os.environ.get('EMAIL_PWD')
        smtp.login(EMAIL_ADDRESS, EMAIL_PWD)
        smtp.sendmail(EMAIL_ADDRESS, mail, msg)


def donormail(city, bloodgroup, link):
    donorlist = Donors.objects.filter(donorCity__iexact=city).filter(donorBloodgroup=bloodgroup)
    subject =  "In need of plasma donation"
    body = f"Hey we have got someone you can donate too https://postgres-app1507.herokuapp.com{link}"
    for donor in donorlist:
        mail(donor.donorMail, subject, body)
        
    
