from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    # path('events/', views.events, name='events'),
    path('events/', views.events, name='events'),
    path('charter/', views.charterHeader, name='citizen'),
    path('media/', views.media, name='medias'),
    path('awards/', views.awards, name='awards'),
    path('gallery/', views.album_list, name='gallery'),
    path('gallery/<int:album_id>/', views.sub_album_list, name='sub_gallery'),
    
    path('think_tank/', views.think_tank, name='think_tank'),
    path('think_tank/<int:think_id>', views.sub_think_tank, name='sub_think_tank'),
]

