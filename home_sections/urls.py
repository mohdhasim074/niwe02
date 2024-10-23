from django.conf.urls.i18n import i18n_patterns

from django.urls import path
from . import views

# urlpatterns = i18n_patterns(
urlpatterns = (
    
    path('related-links/', views.related_links, name='related_links'),
    path('web-policy/', views.website_policy, name='web_ploicy'),
    
)