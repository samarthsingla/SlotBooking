
from django.contrib import admin
from django.urls import path, include
from account import views as account_views
from . import views

urlpatterns = [
    path("<int:sport_id>/", views.view_sport, name="sports-view_sport"),
    path("<int:sport_id>/book/<int:space_id>/", views.booking)
]
