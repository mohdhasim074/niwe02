from django.urls import path
from . import views

urlpatterns = [
    path('rti/', views.rti, name='hi_rti'),
    path('rti/<int:info_id>', views.subInfo, name='hi_subInfo'),

]
