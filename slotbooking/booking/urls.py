
from django.contrib import admin
from django.urls import path, include
# from account import views as account_views
# from sports import urls as sports_urls
from booking import views as booking_views
import booking
urlpatterns = [
   path("editSlots/<int:space_id>", booking_views.edit_slots, name="booking-edit_slots"),
   path("getSlots/", booking_views.get_slots, name="get-slots")
]
