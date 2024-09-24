from django.contrib import admin
from .models import Departments, Reserach_n_Development, Testing_and_Standards_Regulation, Wind_Resources_Assessment, Offshore_Wind_Development, RelatedImage, Finance_and_Administration, Skill_developements_training
from Depart_Section.models import Wind_Terbine_photo, depart_documents, \
    Department_testing_measure, Department_testing_measureType, SDT_workshop, \
    SDT_workshop_type, SDT_vayumitra, \
    SDT_InternationalTraining, SDT_National, \
    SDT_GlobalWindDay, SDT_Webinar, SDT_Customize_Training, SDT_Short_Term, \
    WRA_Sale_publication, WRA_srra_stations, WRA_Numeric_Wind, WRA_Micro_Servey, \
    WRA_Estimated_Potential, WRA_Srra_Station_phases, WRA_Srra_Phase_num,\
    SDT_National_Page, SDT_InternationalTraining_eitec,\
    SDT_InternationalTraining_sub_eitec

# 
# class ImageInline(admin.StackedInline):
#     model = Image

    
@admin.register(Departments)
class DepartmentAdmin(admin.ModelAdmin):
    search_fields = ('id',)

    list_display = ('title', 'description')
    ordering = ['id']


# sdt
@admin.register(Skill_developements_training)
class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    search_fields = ('id',)
    
    ordering = ['id']


# 
@admin.register(Reserach_n_Development)
class RnDAdmin(admin.ModelAdmin):
    search_fields = ('id',)

    list_display = ('title', 'description', 'document_File')
    ordering = ['id']


@admin.register(Testing_and_Standards_Regulation)
class TestingAdmin(admin.ModelAdmin):
    # list_display = ('title', 'description', 'document_File')
    list_display = ('title', 'description')
    search_fields = ('id',)
    
    ordering = ['id']


class WindTerBinephotoAdmin(admin.ModelAdmin):
    list_display = ('image')
    search_fields = ('id',)
    
    ordering = ['id']


admin.site.register(Wind_Terbine_photo)
# 


class Department_Testing_TypeInline(admin.StackedInline):
    model = Department_testing_measureType
    extra = 1


@admin.register(Department_testing_measure)
class DepartTestingMeasureAdmin(admin.ModelAdmin):
    inlines = [Department_Testing_TypeInline]
    search_fields = ('id',)
    ordering = ['id']   


# 
class Workshop_SDT_PhotosInline(admin.TabularInline):
    model = SDT_workshop_type
    extra = 1


@admin.register(SDT_workshop)
class Workshop_SDT(admin.ModelAdmin):
    inlines = [Workshop_SDT_PhotosInline]
    search_fields = ('id',)
    ordering = ['id']   
# 

# 
class SDT_Nationals_pagesInline(admin.StackedInline):
    model = SDT_National_Page
    extra=1


@admin.register(SDT_National)
class SDT_Nationals(admin.ModelAdmin):
    inlines = [SDT_Nationals_pagesInline]
    list_display = ('title', 'id',)
    search_fields=('id',)
    ordering = ['id']


class SDT_InterNational_SubEitc_pagesInline(admin.StackedInline):
    model = SDT_InternationalTraining_sub_eitec
    extra = 1


class SDT_InterNationalEitc_pagesInline(admin.StackedInline):
    inlines = [SDT_InterNational_SubEitc_pagesInline]
    model = SDT_InternationalTraining_eitec
    extra = 1


@admin.register(SDT_InternationalTraining)
class TrainingInternationalAdmin(admin.ModelAdmin):
    inlines = [SDT_InterNationalEitc_pagesInline]
    list_display = ('title',)
    search_fields = ('id',)
    ordering = ['id']


# 
@admin.register(depart_documents)
class departDocumentsAdmin(admin.ModelAdmin): 

    list_display = ('Description', 'Version', 'Download')
    search_fields = ('version', 'id')
    ordering = ['id']


# 
@admin.register(Wind_Resources_Assessment)
class Wind_Res_Admin(admin.ModelAdmin):

    list_display = ('title', 'description')
    ordering = ['id']
    # inlines = [ImageInline]


class RelatedImageInline(admin.StackedInline):
    model = RelatedImage

    
@admin.register(WRA_Sale_publication)
class Wra_Sale_publications(admin.ModelAdmin):
    list_display = ('serial', 'product', 'price',)
    search_fields = ('id',)
    ordering = ['id']

    
@admin.register(WRA_srra_stations)
class Wra_Srra_Stations(admin.ModelAdmin):
    list_display = ('serial', 'state_ut',)
    search_fields = ('id',)
    ordering = ['id']


@admin.register(WRA_Numeric_Wind)
class WRA_Numeric(admin.ModelAdmin):
    list_display = ('domain', 'number_station',)
    search_fields = ('serial',)
    ordering = ('id',)

    
@admin.register(WRA_Micro_Servey)
class WRA_Servey(admin.ModelAdmin):
    list_display = ('state',)
    search_fields = ('serial',)
    ordering = ('id',)

    
@admin.register(WRA_Estimated_Potential)
class WRA_Power_Potential(admin.ModelAdmin):
    list_display = ('serial',)
    search_fields = ('serial',)
    ordering = ('id',)
    
    
class WRA_srra_PhasInline(admin.StackedInline):
    model = WRA_Srra_Phase_num
    extra = 1


@admin.register(WRA_Srra_Station_phases)
class Wra_Srra_phase(admin.ModelAdmin):
    inlines = [WRA_srra_PhasInline]
    
    search_fields = ('station_id',)
    ordering = ['id']
    
    
# 
@admin.register(Offshore_Wind_Development)
class OwdAdmin(admin.ModelAdmin):

    list_display = ('title', 'description')
    ordering = ['id']
    inlines = [RelatedImageInline]


@admin.register(Finance_and_Administration)
class FnAdmin(admin.ModelAdmin):
    list_display = ('description', 'NIWE_Pan_ARN_GST_Details')

    
@admin.register(SDT_vayumitra)
class VayumitraAdmin(admin.ModelAdmin):
    list_display = ('title',)
    ordering = ['id']


@admin.register(SDT_Customize_Training)
class Customized_Training(admin.ModelAdmin):
    list_display = ('title',)
    ordering = ['id']


@admin.register(SDT_GlobalWindDay)
class SDT_Global(admin.ModelAdmin):
    list_display = ('title',)
    ordering = ['id']


@admin.register(SDT_Webinar)
class SDT_Webinars(admin.ModelAdmin):
    list_display = ('title',)
    ordering = ['id']


@admin.register(SDT_Short_Term)
class ShortTermCourses(admin.ModelAdmin):
    list_display = ('title',)
    ordering = ['id']

