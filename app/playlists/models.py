from operator import length_hint
from django.db import models


# class Tutorial(models.Model):
#     title = models.CharField(max_length=70, blank=False, default='')
#     tutorial_url = models.CharField(max_length=200, blank=False, default='')
#     image_path = models.CharField(max_length=150, blank=True, null=True)
#     description = models.CharField(max_length=200, blank=False, default='')
#     published = models.BooleanField(default=False)

class Track(models.Model):
    name = models.CharField(max_length = 70)
    artist = models.TextField(max_length = 70)
    length = models.DecimalField(max_digits = 4, decimal_places = 2)
  
class Playlist(models.Model):
    title = models.CharField(max_length = 70)
    tracks_in_list = models.ManyToManyField(Track)
