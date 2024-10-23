from django.db import models


class CertificationAndInformationTechnologyStaff(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=50, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self): 
        return self.name

    
class CertificationStaffPhoto(models.Model):
    staff = models.ForeignKey(CertificationAndInformationTechnologyStaff, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='subalbums/')
    # 
    Designation = models.CharField(max_length=100, null=True, blank=True)
    Qualification = models.CharField(max_length=100, null=True, blank=True)
    Specialization = models.CharField(max_length=100, null=True, blank=True)
    Areas_Of_Interest = models.CharField(max_length=200, null=True, blank=True)
    Year_of_Joining = models.CharField(max_length=100, null=True, blank=True)
    contact = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=254, unique=True, null=True, blank=True)

    def __str__(self):
        return f"CertificationStaff-Photo of {self.staff.name}"


# 
class DirectorGeneralOfficeStaff(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=50, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self): 
        return self.name


# 
class StaffPhoto(models.Model):
    staff = models.ForeignKey(DirectorGeneralOfficeStaff, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='subalbums/')
        
    Designation = models.CharField(max_length=100, null=True, blank=True)
    Qualification = models.CharField(max_length=100, null=True, blank=True)
    Specialization = models.CharField(max_length=100, null=True, blank=True)
    Areas_Of_Interest = models.CharField(max_length=200, null=True, blank=True)
    Year_of_Joining = models.CharField(max_length=100, null=True, blank=True)
    contact = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=254, unique=True, null=True, blank=True)

    def __str__(self):
        return f"Staff-Photo of {self.staff.name}"


    # 
class OffshoreWindDevelopStaff(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=50, blank=True)

    def __str__(self): 
        return self.name


class OwdStaffPhoto(models.Model):
    staff = models.ForeignKey(OffshoreWindDevelopStaff, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='subalbums/')
    # 
    Designation = models.CharField(max_length=100, null=True, blank=True)
    Qualification = models.CharField(max_length=100, null=True, blank=True)
    Specialization = models.CharField(max_length=100, null=True, blank=True)
    Areas_Of_Interest = models.CharField(max_length=200, null=True, blank=True)
    Year_of_Joining = models.CharField(max_length=100, null=True, blank=True)
    contact = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=254, unique=True, null=True, blank=True)
    def __str__(self):
        return f"OwdStaff-Photo of {self.staff.name}"
        
# 
class TestingStandardsAndRegulationStaff(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=50, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)
    # 
class TestingStaffPhoto(models.Model):
    staff = models.ForeignKey(TestingStandardsAndRegulationStaff, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='subalbums/')
    # 
    Designation = models.CharField(max_length=100, null=True, blank=True)
    Qualification = models.CharField(max_length=100, null=True, blank=True)
    Specialization = models.CharField(max_length=100, null=True, blank=True)
    Areas_Of_Interest = models.CharField(max_length=200, null=True, blank=True)
    Year_of_Joining = models.CharField(max_length=100, null=True, blank=True)
    contact = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=254, unique=True, null=True, blank=True)
    def __str__(self):
        return f"TestingStaff-Photo of {self.staff.name}"

# 
class ResearchAndDevelopmentStaff(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=50, blank=True)
    
    # 
class ResearchStaffPhoto(models.Model):
    staff = models.ForeignKey(ResearchAndDevelopmentStaff, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='subalbums/')
    # 
    Designation = models.CharField(max_length=100, null=True, blank=True)
    Qualification = models.CharField(max_length=100, null=True, blank=True)
    Specialization = models.CharField(max_length=100, null=True, blank=True)
    Areas_Of_Interest = models.CharField(max_length=200, null=True, blank=True)
    Year_of_Joining = models.CharField(max_length=100, null=True, blank=True)
    contact = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=254, unique=True, null=True, blank=True)

    def __str__(self):
        return f"ResearchStaff-Photo of {self.staff.name}"

# 
class WindResourceAssessmentStaff(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=50, blank=True)

# 
class WRAStaffPhoto(models.Model):
    staff = models.ForeignKey(WindResourceAssessmentStaff, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='subalbums/')
    # 
    Designation = models.CharField(max_length=100, null=True, blank=True)
    Qualification = models.CharField(max_length=100, null=True, blank=True)
    Specialization = models.CharField(max_length=100, null=True, blank=True)
    Areas_Of_Interest = models.CharField(max_length=200, null=True, blank=True)
    Year_of_Joining = models.CharField(max_length=100, null=True, blank=True)
    contact = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=254, unique=True, null=True, blank=True)

    def __str__(self):
        return f"WRAStaff-Photo of {self.staff.name}"
# 
class SkillDevelopmentAndTrainingStaff(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    email = models.EmailField(max_length=254, unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=50, blank=True)

class SDTStaffPhoto(models.Model):
    staff = models.ForeignKey(SkillDevelopmentAndTrainingStaff, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='subalbums/')
    # 
    Designation = models.CharField(max_length=100, null=True, blank=True)
    Qualification = models.CharField(max_length=100, null=True, blank=True)
    Specialization = models.CharField(max_length=100, null=True, blank=True)
    Areas_Of_Interest = models.CharField(max_length=200, null=True, blank=True)
    Year_of_Joining = models.CharField(max_length=100, null=True, blank=True)
    contact = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=254, unique=True, null=True, blank=True)

    def __str__(self):
        return f"SDTStaff-Photo of {self.staff.name}"

# 
class FinanceAndAdministrationStaff(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    email = models.CharField(max_length=254, unique=True, null=True, blank=True)
    phone_number = models.CharField(max_length=50, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)

# 
class FinanceStaffPhoto(models.Model):
    staff = models.ForeignKey(FinanceAndAdministrationStaff, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='subalbums/')
    # 
    Designation = models.CharField(max_length=100, null=True, blank=True)
    Qualification = models.CharField(max_length=100, null=True, blank=True)
    Specialization = models.CharField(max_length=100, null=True, blank=True)
    Areas_Of_Interest = models.CharField(max_length=200, null=True, blank=True)
    Year_of_Joining = models.CharField(max_length=100, null=True, blank=True)
    contact = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=254, unique=True, null=True, blank=True)

    def __str__(self):
        return f"FinanceStaff-Photo of {self.staff.name}"
