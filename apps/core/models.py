# apps/core/apps.py

# Django modules
from django.db import models

# Create your models here.

class TimeStampedModel(models.Model):

    """ Time Stamped Model 
		This model can be used in any app
		in order not to REPEATING 
		creating the same fields in the models.
    """

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True