from django.urls import path
from . import views

urlpatterns = [

    path('about_background/', views.hi_about_background, name='hi_background'),
    path('about_charter/', views.hi_about_charter, name='hi_charter'),
    path('about_dgm/', views.hi_about_dgm, name='hi_dgm'),
    path('about_org/', views.hi_about_org, name='hi_org'),
    path('about_qlty_ply/', views.hi_about_qlty_ply, name='hi_quality'),
    path('about_us/', views.hi_about_us, name='hi_us'),
]