from django.contrib import admin
from .models import Award, Citizen_Charter, Events, SubGallery, Gallery, Sub_Think_Tank, Think_Tank


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
class SubGalleryInline(admin.TabularInline):
    model = SubGallery
    extra = 1

class GalleryAdmin(admin.ModelAdmin):
    inlines = [SubGalleryInline]
    list_display=('title', 'id',)
    
    ordering = ['id']
admin.site.register(Gallery, GalleryAdmin)


class Sub_Think_TankInline(admin.TabularInline):
    model = Sub_Think_Tank
    extra = 1

class Think_TankAdmin(admin.ModelAdmin):
    inlines = [Sub_Think_TankInline]
    list_display=('title', 'id',)
    ordering = ['id']

admin.site.register(Think_Tank, Think_TankAdmin)

