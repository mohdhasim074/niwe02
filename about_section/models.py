from django.db import models
from tinymce.models import HTMLField
# 
class AboutUs(models.Model):
    title = models.CharField()
    description = HTMLField()
# 
class DirectorGeneralMessage(models.Model):
    title = models.CharField()
    Dirs_image = models.FileField(upload_to="images/", null=True, default=None)
    description = HTMLField()
# 
class Background(models.Model):
    description = HTMLField()    
# 
class charter(models.Model):
    preamble = HTMLField()
    mission = HTMLField()
    objectives = HTMLField()
    # 
class OrganizationalChart(models.Model):
    description = HTMLField()
    image = models.FileField(upload_to='images/', null=True, default=None)
# 
class QualityPolicy(models.Model):
    policyImage =  models.FileField(upload_to='images/', null=True, default=None)


