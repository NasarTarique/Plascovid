from django.contrib import admin
from .models import Hospitals,  Donors, Receivers

# Register your models here.

admin.site.register(Hospitals)
admin.site.register(Donors)
admin.site.register(Receivers)

