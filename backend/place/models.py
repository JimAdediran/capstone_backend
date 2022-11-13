from random import choices
from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

region_choices = (
    ('west', 'WEST'),
    ('east', 'EAST'),
    ('south', 'SOUTH'),
    ('alaska', 'ALASKA'),
    ('hawaii', 'HAWAII'),
    ('midwest', 'MIDWEST'),
)

class Place(models.Model):
    region = models.CharField(max_length=7, choices=region_choices)
