from django.db import models

class Recruitment(models.Model):
    
    recruitmentTitle = models.CharField(max_length=200)
    recruitmentNotification = models.FileField(upload_to=None, max_length=100, null=True, blank=True) 
    
class RecruitmentDetails(models.Model):

    srNo = models.IntegerField()
    advertisementNo = models.CharField(max_length=50)
    nameOfPost = models.CharField(max_length=100)
    dateExtension = models.CharField(max_length=150, null=True, blank=True)
    applicationForm = models.FileField(upload_to='pdf/', max_length=100, null=True, blank=True)

class Status(models.Model):

    nameOfPost = models.CharField(max_length=100)
    status1 = models.FileField(upload_to='pdf/', max_length=100, null=True, blank=True)
    status2 = models.FileField(upload_to='pdf/', max_length=100, null=True, blank=True)

class Result(models.Model):

    advertisementNo = models.CharField(max_length=50)
    resultDescription = models.CharField(max_length=150, null=True, blank=True)
    result = models.FileField(upload_to='pdf/', max_length=100, null=True, blank=True)

class Cancellation(models.Model):
    cancellationTitle = models.CharField(max_length=100)
    cancellationNotification = models.FileField(upload_to='pdf/', max_length=100)
