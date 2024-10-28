from tinymce.models import HTMLField
from django.db import models

class RightToInformation(models.Model):

    # title = models.CharField(max_length=255)
    year = models.CharField(max_length=20, null=True, blank=True)
    document = models.FileField(upload_to='pdf/', null=True, blank=True)
  
class Information(models.Model):
    serial = models.IntegerField(default=1)
    title = models.CharField(max_length=250, null=True, blank=True)
    document = models.FileField(upload_to='pdf/', null=True, blank=True)
    # url=models.URLField(null=True, blank=True)
    
def __str__(self):
        return self.title
    
class subInformation(models.Model):
    item = models.ForeignKey(Information, on_delete=models.CASCADE)
    description = HTMLField(null=True, blank=True)
    