from django.urls import path
from . import views

urlpatterns = [
    
    path('related-links/', views.related_links, name='related_link'),
    
]