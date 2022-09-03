from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path("login", views.account_login, name="account-login"), 
    path("register", views.account_register, name="account-register"),
    path("logout", views.account_logout, name="account-logout"),
    path("profile", views.account_profile, name="account-profile"),
]