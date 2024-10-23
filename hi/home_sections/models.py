from django.db import models
from tinymce.models import HTMLField

# Create your models here.


# 
class Related_links(models.Model):
    title = models.CharField(max_length=250)
    area=models.CharField(max_length=20, default='India')
    description = HTMLField(blank=True) 
    