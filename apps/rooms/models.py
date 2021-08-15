# apps/rooms/models.py

# Django modules
from django.db import models
from django_countries.fields import CountryField

# Locals
from apps.core.models import MyAbstractTimeStamped
from apps.users.models import MyCustomUser

# Create your models here.

# AbstractItem model
class AbstractItem(MyAbstractTimeStamped):

    """ Abstract Item """

    name = models.CharField(max_length=80)

    """ 
    --------As its name AbstractItem, it will not be seen in admin dashboard--------

    """

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


# RoomType model
class RoomType(AbstractItem):

    """ RoomType Model Definition """

    """ 
    --------After running the migrations the real fields will be as seen bellow--------
    name='RoomType',
    fields=[
        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        ('created', models.DateTimeField(auto_now_add=True)),
        ('updated', models.DateTimeField(auto_now=True)),
        ('name', models.CharField(max_length=80)),
    ],
    """

    class Meta:
        verbose_name = "Room Type"


# Amenity model
class Amenity(AbstractItem):

    """ Amenity Model Definition """

    """ 
    --------After running the migrations the real fields will be as seen bellow--------
    name='Amenity',
    fields=[
        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        ('created', models.DateTimeField(auto_now_add=True)),
        ('updated', models.DateTimeField(auto_now=True)),
        ('name', models.CharField(max_length=80)),
    ],
    """

    class Meta:
        verbose_name_plural = "Amenities"



# Facility model
class Facility(AbstractItem):

    """ Facility Model Definition """

    """ 
    --------After running the migrations the real fields will be as seen bellow--------
    name='Facility',
    fields=[
        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        ('created', models.DateTimeField(auto_now_add=True)),
        ('updated', models.DateTimeField(auto_now=True)),
        ('name', models.CharField(max_length=80)),
    ],
    """
    class Meta:
        verbose_name_plural = "Facilities"



# HouseRule model
class HouseRule(AbstractItem):

    """ HouseRule Model Definition """

    """ 
    --------After running the migrations the real fields will be as seen bellow--------
    name='HouseRule',
    fields=[
        ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
        ('created', models.DateTimeField(auto_now_add=True)),
        ('updated', models.DateTimeField(auto_now=True)),
        ('name', models.CharField(max_length=80)),
    ],
    """
    class Meta:
        verbose_name = "House Rule"



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
    room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True)
    amenities = models.ManyToManyField(Amenity, blank=True)
    facilities = models.ManyToManyField(Facility, blank=True)
    house_rules = models.ManyToManyField(HouseRule, blank=True)

    def __str__(self):
        return self.name
