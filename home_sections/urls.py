from django.urls import path
from . import views

urlpatterns = [
    
    path('related-links/', views.related_links, name='related_link'),
    path('web-policy/', views.website_policy, name='web_ploicy'),
    
]