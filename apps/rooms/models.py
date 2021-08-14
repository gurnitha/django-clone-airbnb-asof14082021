# apps/rooms/models.py

# Django modules
from django.db import models
from django_countries.fields import CountryField

# Locals
from apps.core.models import MyAbstractTimeStamped
from apps.users.models import MyCustomUser

# Create your models here.

# AbstractItem model

# Room model
class Room(MyAbstractTimeStamped):

    """ Room Model Definition """

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(MyCustomUser, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
