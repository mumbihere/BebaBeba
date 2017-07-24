from django.db import models
from django.utils import timezone

class Driver(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)

    class Meta:
        ordering = ["-name"]

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Passenger(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    class Meta:
        ordering = ["-name"]

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Payment(models.Model):
    passenger = models.ForeignKey('Passenger', on_delete=models.CASCADE)
    date = models.DateTimeField('date booked',default=timezone.now)
    amount  = models.IntegerField(default=0)
    # class Meta:
    #     abstract = True
    def __str__(self):              # __unicode__ on Python 2
        return self.id

class Booking(models.Model):
	driver = models.ForeignKey('Driver', on_delete=models.CASCADE)
	passenger = models.ForeignKey('Passenger', on_delete=models.CASCADE, blank=True)
	date = models.DateTimeField('date booked' ,default=timezone.now)  

    # votes = models.IntegerField(default=0)