from django.db import models
from tinymce.models import HTMLField

class ContactUs(models.Model):

    feedback_and_Address = HTMLField()
    testing_and_Research_Station = HTMLField()
    
