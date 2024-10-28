from django.contrib import admin
from django import forms
from Document_Section.models import  WEG_Installation_Details_India, \
    weg_install_world_wise, Newsletters
from . models import Documents, RecordsRetentionSchedule, GeneralInformation, RevisedGuidelinesForProject, AnnualReport, ComparisonBetweenFosilFuelAndWind, FAQs, RelatedLinks


@admin.register(Documents)
class DocumentAdmin(admin.ModelAdmin):

    list_display = ('title', 'description')
    ordering = ['id']


# 
@admin.register(GeneralInformation)
class GenInfoAdmin(admin.ModelAdmin):

    list_display = ('title', 'description')
    ordering = ['id']

# 
@admin.register(ComparisonBetweenFosilFuelAndWind)
class DiffAdmin(admin.ModelAdmin):

    list_display = ('heading', 'fosil_Fuel', 'Wind_Energy')
    ordering = ['id']


@admin.register(RevisedGuidelinesForProject)
class RevisedGuidelinesAdmin(admin.ModelAdmin):

    list_display = ('sr_No', 'title', 'date')
    search_fields= ('sr_No', )
    ordering = ['id']


@admin.register(RecordsRetentionSchedule)
class RecordsRetentionScheduleAdmin(admin.ModelAdmin):

    list_display = ('ministry_Approval', 'NIEW_Records_Retention_Schedule')
    ordering = ['id']
# 
@admin.register(Newsletters)
class NewslettersAdmin(admin.ModelAdmin):
    list_display = ('issue', 'year')
    search_fields = ('issue', 'year')
    list_filter=('id','issue')
    ordering = ['id']



# 
@admin.register(AnnualReport)
class AnnualReportAdmin(admin.ModelAdmin): 

    list_display = ('image', 'year')
    search_fields = ('image', 'year')
    ordering = ['id']


@admin.register(RelatedLinks)
class RelatedLinksAdmin(admin.ModelAdmin):

    list_display = ('title', 'linkTitle')
    ordering = ['id']


@admin.register(FAQs)
class FaqAdmin(admin.ModelAdmin):

    list_display = ('preamble', 'Faq')
    ordering = ['id']

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        # Check if the form contains the 'preamble' field before modifying it
        if 'preamble' in form.base_fields:
            if self.model.objects.exists() and not obj:
                form.base_fields['preamble'].widget = forms.HiddenInput()
        return form

    def save_model(self, request, obj, form, change):
        if not change and self.model.objects.exists():
            obj.preamble = None  # Ensure preamble is not duplicated
        super().save_model(request, obj, form, change)

    def get_readonly_fields(self, request, obj=None):
        if self.model.objects.exists() and not obj:
            return self.readonly_fields + ('preamble',)
        return self.readonly_fields


# india year-wise
class WEG_Installation_Details_IndiaAdmin(admin.ModelAdmin):
    list_display = (
        'sr_no', 'state', 'upto_31_03_2002', 'year_2002_03', 'year_2003_04',
        'year_2004_05', 'year_2005_06', 'year_2006_07', 'year_2007_08', 'year_2008_09',
        'year_2009_10', 'year_2010_11', 'year_2011_12', 'year_2012_13', 'year_2013_14',
        'year_2014_15', 'year_2015_16', 'year_2016_17', 'year_2017_18', 'year_2018_19',
        'year_2019_20', 'year_2020_21', 'year_2021_22'
    )
    search_fields = ('state',)
    list_filter = ('state',)
    ordering = ('sr_no',)


admin.site.register(WEG_Installation_Details_India, WEG_Installation_Details_IndiaAdmin)


    # world-wise
class weg_install_world_wiseAdmin(admin.ModelAdmin):
    list_display = (
        'position', 'country', 'capacity'
    ) 
    search_fields = ('country',)
    list_filter = ('country',)
    ordering = ('capacity',)


admin.site.register(weg_install_world_wise, weg_install_world_wiseAdmin)
