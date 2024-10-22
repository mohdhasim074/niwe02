from django.contrib import admin
from .models import RightToInformation, Information, subInformation

@admin.register(RightToInformation)
class RtiAdmin(admin.ModelAdmin):

    list_display = ( 'year', 'document')
    list_filter = ('id',)
    ordering = ['id']

class InformationInline(admin.StackedInline):
    model =subInformation
    extra =1 

class InfoAdmin(admin.ModelAdmin):
    inlines= [InformationInline]
    list_display=('title','id',)
    list_filter  =  ('id',)
    search_fields  =  ('title', 'id',)
    ordering  =  ['serial']
    
admin.site.register(Information, InfoAdmin)