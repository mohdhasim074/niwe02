from django.contrib import admin
from .models import Award, Citizen_Charter, Events, Album, SubAlbum


@admin.register(Award)
class AwardAdmin(admin.ModelAdmin):

    list_display = ('title', 'description', 'image_Tag')
    ordering = ['id']


@admin.register(Citizen_Charter)
class Citi_Chart_Admin(admin.ModelAdmin):

    list_display = ('title', 'document_File') 


@admin.register(Events)
class EventsAdmin(admin.ModelAdmin):

    list_display = ('title', 'document_File', 'url')
    ordering = ['id']

    
    # 
class SubAlbumInline(admin.TabularInline):
    model = SubAlbum
    extra = 1

class AlbumAdmin(admin.ModelAdmin):
    inlines = [SubAlbumInline]
    ordering = ['id']

admin.site.register(Album, AlbumAdmin)

