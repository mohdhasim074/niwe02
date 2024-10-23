from django.db import models
from tinymce.models import HTMLField

# Create your models here.
# class Intro(models.Model):
#     title = models.CharField()
#     description = HTMLField()
# # 


# 
class Certification_Procedure(models.Model):
    title = models.CharField(max_length=250)
    description = HTMLField()
