from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # path('events/', views.events, name='events'),
    path('events/', views.events, name='hi_events'),
    path('charter/', views.charterHeader, name='hi_citizen'),
    path('media/', views.media, name='hi_medias'),
    path('awards/', views.awards, name='hi_awards'),
    path('gallery/', views.album_list, name='hi_gallery'),
    path('gallery/<int:album_id>/', views.sub_album_list, name='hi_sub_gallery'),
    
    path('think_tank/', views.think_tank, name='hi_think_tank'),
    path('think_tank/<int:think_id>', views.sub_think_tank, name='hi_sub_think_tank'),
]
 
