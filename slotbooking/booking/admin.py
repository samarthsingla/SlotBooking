from django.contrib import admin
from .models import Availability, Slot, Booking, Space
# Register your models here.
admin.site.register(Space)
admin.site.register(Availability)
admin.site.register(Slot)
admin.site.register(Booking)

