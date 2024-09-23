from django.contrib import admin
from .models import Recruitment, RecruitmentDetails, Status, Result, Cancellation

@admin.register(Recruitment)
class RecruitmentAdmin(admin.ModelAdmin):
    list_display = ('recruitmentTitle', 'recruitmentNotification')
    ordering = ['id']

@admin.register(RecruitmentDetails)
class RecruitmentDetailsAdmin(admin.ModelAdmin):

    list_display = ('srNo', 'advertisementNo', 'nameOfPost', 'dateExtension', 'applicationForm')
    ordering = ['srNo']

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):

    list_display = ('nameOfPost', 'status1', 'status2')
    ordering = ['id']

@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):

    list_display = ('advertisementNo', 'resultDescription', 'result')
    ordering = ['id']

@admin.register(Cancellation)
class CancellationAdmin(admin.ModelAdmin):

    list_display = ('cancellationTitle', 'cancellationNotification')
    ordering = ['id']




