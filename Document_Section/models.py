from django.db import models
from tinymce.models import HTMLField


class Documents(models.Model):

    title = models.CharField(max_length=250)
    description = HTMLField()


# 
class GeneralInformation(models.Model):
    title = models.CharField(max_length=250)
    description = HTMLField(blank=True)


# 
class ComparisonBetweenFosilFuelAndWind(models.Model):

    heading = models.CharField()
    fosil_Fuel = HTMLField()
    Wind_Energy = HTMLField()





# 
class RevisedGuidelinesForProject(models.Model):
     
    sr_No = models.IntegerField()
    description = HTMLField()
    date = models.DateField(auto_now=False, auto_now_add=False)


class RecordsRetentionSchedule(models.Model):
    ministry_Approval = models.FileField(upload_to='pdf/')
    NIEW_Records_Retention_Schedule = models.FileField(upload_to='pdf/')

#


class Newsletters(models.Model):
    issue = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    docs = models.FileField(upload_to='pdf/')

    def __str__(self):
        return self.issue

    def get_docs_url(self):
        return self.docs.url  # Returns the URL of the uploaded file


#    
class AnnualReport(models.Model):
    year = models.CharField(max_length=100)
    image = models.ImageField(upload_to='annual-reports/')
    docs = models.FileField(upload_to='annual-reports/')


def __str__(self):
     return self.year


def get_docs_url(self):
        return self.docs.url  # Returns the URL of the uploaded file


# 
class RelatedLinks(models.Model):

     title = models.CharField()
     linkTitle = HTMLField()


class FAQs(models.Model):
     preamble = HTMLField(null=True, blank=True)
     Faq = HTMLField()

#  for table year-wise-country


class WEG_Installation_Details_India(models.Model):
    sr_no = models.IntegerField()
    state = models.CharField(max_length=100)
    upto_31_03_2002 = models.DecimalField(max_digits=10, decimal_places=2)
    year_2002_03 = models.DecimalField(max_digits=10, decimal_places=2)
    year_2003_04 = models.DecimalField(max_digits=10, decimal_places=2)
    year_2004_05 = models.DecimalField(max_digits=10, decimal_places=2)
    year_2005_06 = models.DecimalField(max_digits=10, decimal_places=2)
    year_2006_07 = models.DecimalField(max_digits=10, decimal_places=2)
    year_2007_08 = models.DecimalField(max_digits=10, decimal_places=2)
    year_2008_09 = models.DecimalField(max_digits=10, decimal_places=2)
    year_2009_10 = models.DecimalField(max_digits=10, decimal_places=2)
    year_2010_11 = models.DecimalField(max_digits=10, decimal_places=2)
    year_2011_12 = models.DecimalField(max_digits=10, decimal_places=2)
    year_2012_13 = models.DecimalField(max_digits=10, decimal_places=2)
    year_2013_14 = models.DecimalField(max_digits=10, decimal_places=2)
    year_2014_15 = models.DecimalField(max_digits=10, decimal_places=2)
    year_2015_16 = models.DecimalField(max_digits=10, decimal_places=2)
    year_2016_17 = models.DecimalField(max_digits=10, decimal_places=2)
    year_2017_18 = models.DecimalField(max_digits=10, decimal_places=2)
    year_2018_19 = models.DecimalField(max_digits=10, decimal_places=2)
    year_2019_20 = models.DecimalField(max_digits=10, decimal_places=2)
    year_2020_21 = models.DecimalField(max_digits=10, decimal_places=2)
    year_2021_22 = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.state} - {self.sr_no}"


#  for country world-wise
class weg_install_world_wise(models.Model):
    position = models.IntegerField()
    country = models.CharField(max_length=100)
    capacity = models.IntegerField()
     
# newslateers.

# annual reports.

