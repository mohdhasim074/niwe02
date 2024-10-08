from django.db import models
from tinymce.models import HTMLField
from django.utils.html import format_html

# awards
class Award(models.Model):
     title = models.CharField()
     description = HTMLField()
     image_1 = models.FileField(upload_to='images/', null=True, blank=True)
     image_2 = models.FileField(upload_to='images/', null=True, blank=True)

     def image_Tag(self):
          return format_html('<img src="/static/{}" style="width:40px;height:40px;border-radius:50%;" />'.format(self.image_1))
     
     image_Tag.short_description = 'Image'

class Citizen_Charter(models.Model):
     
     title = models.CharField(default="Citizen Charter")
     document_File = models.FileField(upload_to='pdf/', max_length=100)

# events
class Events(models.Model):

     title = models.CharField()
     document_File = models.FileField(upload_to='pdf/', max_length=100, blank=True)
     url = models.URLField(blank=True, null=True, default="Empty")


# for gallery/sub-gallery 


class Gallery(models.Model):
    title = models.CharField(max_length=255)
    cover_image = models.ImageField(upload_to='albums/')

    def __str__(self): 
        return self.title

 
class SubGallery(models.Model):
    album = models.ForeignKey(Gallery, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='subalbums/')

    def __str__(self):
        return f"Sub-Gallery of {self.album.title}"

 
class Think_Tank(models.Model):
    title = models.CharField(max_length=155)
#     cover_image = models.ImageField(upload_to='albums/')

    def __str__(self): 
        return self.title

 
class Sub_Think_Tank(models.Model):
    album = models.ForeignKey(Think_Tank, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='subalbums/')

    def __str__(self):
        return f"Sub-Think-tank of {self.album.title}"

 