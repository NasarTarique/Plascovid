from django.urls import path 

from . import views 

urlpatterns = [
    path('', views.index, name="index"),
    path('selfassesment', views.selfassesment, name="selfassesment"),
    path('contact', views.contact, name="contact"),
    path('donorform', views.donor, name="donorform"),
    path('register', views.register, name="register"),
    path('submissions', views.submissions, name='submissions'),
    path('donorinfo', views.donorinfo, name='donorinfo'),
    path('userform', views.userform, name='userform'),
]
