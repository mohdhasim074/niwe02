from django.db import models
from tinymce.models import HTMLField
from django.utils.text import slugify


# Create your models here.\

# departments
class Departments(models.Model):
    title = models.CharField()
    description = HTMLField()


# research 
class Reserach_n_Development(models.Model):
    title = models.CharField()
    description = HTMLField(null=True, blank=True)
    document_File = models.FileField(upload_to='pdf/', null=True, blank=True)


# testing
class Testing_and_Standards_Regulation(models.Model):
    title = models.CharField(max_length=255)  # max_length is required
    description = HTMLField(null=True, blank=True)
    # document_File = models.FileField(upload_to="pdf/", null=True, blank=True)

    
class Wind_Terbine_photo(models.Model):
    terbine_photo = models.ImageField(upload_to='subalbums/')


# 
# 
class depart_documents(models.Model):
    Description	 = models.CharField(max_length=100)
    Version = models.DecimalField(max_digits=10, decimal_places=2)
    Download	 = models.FileField(upload_to='departs/')


# Skill_developements_training
class Skill_developements_training(models.Model):
    title = models.CharField(max_length=255)  # max_length is required
    description = HTMLField(null=True, blank=True)

    
class Department_testing_measure(models.Model): 
    title = models.CharField(max_length=100)

    
class Department_testing_measureType(models.Model):
    item = models.ForeignKey(Department_testing_measure, on_delete=models.CASCADE)
    s_no = models.IntegerField()
    year = models.CharField(max_length=100)
    project_number = 	 models.CharField(max_length=100)
    testing_type_with_company_name = models.CharField(max_length=100)
    agreement_signed = models.DateField(auto_now=False, auto_now_add=False)
   
    def __str__(self):
        return f"Department-testing  of {self.item.title}"


class SDT_Customize_Training(models.Model):
    serial = models.IntegerField()
    title = models.CharField(max_length=255)
    # link = models.URLField()


class SDT_Customize_Training_Sub(models.Model):
    item = models.ForeignKey(SDT_Customize_Training, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    data = HTMLField(null=True, blank=True)

    def __str__(self):
        return f"National-training  of {self.item.title}"
 
    
class SDT_Webinar(models.Model):
    title = models.CharField(max_length=255,)
    image = models.ImageField(upload_to='images/')
    docs = models.FileField(upload_to='annual-reports/')

    def __str__(self):
        return self.title

    def get_url_url(self):
        return self.docs.url  # Returns the URL of the uploaded file


class SDT_Short_Term(models.Model):
    title = models.CharField(max_length=255,)
    image = models.ImageField(upload_to='images/')
    description = HTMLField(null=True, blank=True)

    def __str__(self):
        return self.title

    
class SDT_GlobalWindDay(models.Model):
    serial = models.IntegerField()
    title = models.CharField(max_length=255)
    url = models.URLField()

    def __str__(self):
     return self.title

    def get_url_url(self):
        return self.url.url  # Returns the URL of the uploaded file


class SDT_workshop(models.Model):
    url = models.CharField(max_length=255)  # max_length is required
    title = models.CharField(max_length=255)  # max_length is required


class SDT_workshop_type(models.Model):
    item = models.ForeignKey(SDT_workshop, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f"workshop-testing  of {self.item.title}"

    
class SDT_National(models.Model):
    serial = models.IntegerField()
    title = models.CharField(max_length=200)


class SDT_National_Page(models.Model):
    item = models.ForeignKey(SDT_National, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    data = HTMLField(null=True, blank=True)

    def __str__(self):
        return f"National-training  of {self.item.title}"


class SDT_InternationalTraining(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)  # Add slug field
    image = models.ImageField(upload_to='annual-reports/')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class SDT_InternationalTraining_eitec(models.Model):
    item = models.ForeignKey(SDT_InternationalTraining, on_delete=models.CASCADE)
    serial = models.IntegerField()
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)  # Add slug field

    def __str__(self):
        return f"{self.serial}. {self.title} ({self.item.title})"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class SDT_InternationalTraining_sub_eitec(models.Model):
    eitec = models.ForeignKey(SDT_InternationalTraining_eitec, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)  # Add slug field
    data = HTMLField(null=True, blank=True)

    def __str__(self):
        return f"International Sub EITEC training of {self.eitec.item.title} - {self.title}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    
class SDT_vayumitra(models.Model):
    serial = models.IntegerField()
    title = models.CharField(max_length=255)
    docs = models.FileField(upload_to='annual-reports/')

    def __str__(self):
        return self.title


# 
#  Wind_Resources_Assessment
class Wind_Resources_Assessment(models.Model):
    title = models.CharField(max_length=255)  # max_length is required
    description = HTMLField(null=True, blank=True)


class WRA_Sale_publication(models.Model):
    serial = models.IntegerField()
    product = models.CharField(max_length=250)
    price = models.CharField(max_length=250)
    total_amount1 = models.CharField(max_length=250)
    total_amount2 = models.CharField(max_length=250)
    charge = models.CharField(max_length=250)
    remarks = models.CharField(max_length=250)


class WRA_srra_stations(models.Model):
    serial = models.IntegerField()
    state_ut = models.CharField(max_length=250)
    phase1 = models.CharField(max_length=250)
    phase2 = models.CharField(max_length=250)
    ams = models.CharField(max_length=250)
    meda = models.CharField(max_length=250)
    anert = models.CharField(max_length=250)
    total = models.CharField(max_length=250)


class WRA_Numeric_Wind(models.Model):
    serial = models.IntegerField()
    domain = models.CharField(max_length=250)
    number_station = models.IntegerField()
    error_of_wind_speed = models.DecimalField(max_digits=10, decimal_places=2)


class WRA_Micro_Servey(models.Model):
    serial = models.IntegerField()
    state = models.CharField(max_length=250)
    stations = models.IntegerField()


class WRA_Estimated_Potential(models.Model):
    serial = models.IntegerField()
    state_ut = models.CharField(max_length=250)
    potential_50m = models.IntegerField()
    potential_80m = models.IntegerField()
    # 


class WRA_Srra_Station_phases(models.Model):
    head = models.CharField(max_length=250)
    phase_type = models.CharField(max_length=250)
    
    station_id = models.IntegerField()
    station_name = models.CharField(max_length=250)
    location = models.CharField(max_length=250)
    district = models.CharField(max_length=250)
    state = models.CharField(max_length=250)
    comission_date = models.DateField(auto_now=False, auto_now_add=False)
    latitude = models.DecimalField(max_digits=10, decimal_places=3)
    longitude = models.DecimalField(max_digits=10, decimal_places=3)
    elavation = models.IntegerField()  


# owd
class Offshore_Wind_Development(models.Model):
    title = models.CharField(max_length=250)
    description = HTMLField()


class RelatedImage(models.Model):
    OWD = models.ForeignKey(Offshore_Wind_Development, related_name='images', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='images/')


#  finance
class Finance_and_Administration(models.Model):

    description = HTMLField()
    NIWE_Pan_ARN_GST_Details = HTMLField()
    
