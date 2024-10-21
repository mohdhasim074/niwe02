from django.db import models
from tinymce.models import HTMLField

# Create your models here.


# 
class Related_links(models.Model):
    title = models.CharField(max_length=250)
    area=models.CharField(max_length=20, default='India')
    description = HTMLField(blank=True) 
    

class CorporateFilm(models.Model):
    title = models.CharField(max_length=200, default="Corporate film about NIWE")
    video_url = models.URLField()  # YouTube or Vimeo link
    hindi_version_url = models.URLField()  # URL for Hindi version