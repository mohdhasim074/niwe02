from django.db import models

class RightToInformation(models.Model):

    title = models.CharField(max_length=255)
    year = models.CharField(max_length=20, null=True, blank=True)
    document = models.FileField(upload_to='pdf/', null=True, blank=True)
