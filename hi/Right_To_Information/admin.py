from django.contrib import admin
from .models import RightToInformation

@admin.register(RightToInformation)
class RtiAdmin(admin.ModelAdmin):

    list_display = ('title', 'year', 'document')
    #list_filter = ('title',)
    ordering = ['id']
