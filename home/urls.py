from django.urls import path
from django.contrib import admin
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("login", views.login_user, name='login'),
    path("logout", views.logout_user, name='logout'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'),
    path("dashboard", views.calculate_distance_view, name='dashboard')
]
