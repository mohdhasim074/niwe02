from django.urls import path
from . import views

urlpatterns = [
    
    path('download/', views.download, name='document'),
    path('azadi_ka_amrit_mahotsav/', views.azadi_ka_amrit_mahotsav, name='amrit_mahotsav'),
    path('information_gi/', views.information_gi, name='GenInfo'),
    path('information_hwed/', views.information_hwed, name='hwed'),
    path('record_retention/', views.record_retention, name='retention'),
    path('relatedlinks/', views.relatedlinks,name='related_links'),
    path('faq/', views.faq, name='faq'),
    path('power_policy', views.wind_power_policy, name='power_policy'),
   

]

