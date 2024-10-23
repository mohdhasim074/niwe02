from django.contrib import admin
from . models import *

# Register your models here.

@admin.register(Related_links)
class RelatedLinksAdmin(admin.ModelAdmin):

    list_display = ('title', 'description')
    ordering = ['id']