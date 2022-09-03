from django.db import models
# Create your models here.

class Sport(models.Model):
    sport_name = models.CharField(verbose_name="Name of the Sport", max_length=20)
    accepting_bookings = models.BooleanField(default=True)

    def __str__(self):
        return self.sport_name
    


class Equipment(models.Model):
    pass
