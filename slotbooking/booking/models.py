from django.db import models
from sports.models import Sport
import datetime
from account.models import Account

class Slot(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return str(self.id) + " " +  str(self.start_time) + " " + str(self.end_time)

class Space(models.Model):
    name = models.CharField(max_length=30, verbose_name="Space Name")
    assoc_sport = models.ForeignKey(Sport, on_delete=models.CASCADE, verbose_name="Associated Sport")
    total_units = models.IntegerField()
    available = models.BooleanField(default=True)
    slots = models.ManyToManyField(Slot, through='Availability')
    
    def __str__(self):
        return self.name + " | " + self.assoc_sport.sport_name

class Availability(models.Model):
    #junction table containing information about slots on particular days
    space = models.ForeignKey(Space, on_delete=models.CASCADE)
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE, null=True)
    date = models.DateField(null=True)
    units_available = models.IntegerField(default=1)
    class Meta:
        unique_together = [['space', 'slot', 'date']]


class Request(models.Model):
    pass

class Booking(models.Model):    
    availability = models.ForeignKey(to=Availability, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE, default=Account.objects.filter(type = "admin").first())
    # slotInfoObj = models.ForeignKey(SlotInfo, on_delete=models.CASCADE, null=True)


