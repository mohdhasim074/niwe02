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


class Album(models.Model):
    title = models.CharField(max_length=255)
    cover_image = models.ImageField(upload_to='albums/')

    def __str__(self): 
        return self.title

 
class SubAlbum(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='subalbums/')

    def __str__(self):
        return f"Sub-Album of {self.album.title}"

 