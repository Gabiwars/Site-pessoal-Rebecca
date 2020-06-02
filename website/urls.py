from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('contact.html', views.contact, name="contact"),
    path('about.html', views.about, name="about"),
    path('appointment.html', views.appointment, name="appointment"),
    path('gallery.html', views.gallery, name="gallery"),

]
