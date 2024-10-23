from django.urls import path
from . import views

urlpatterns = [
    path('career/', views.hi_careers, name='hi_career'),
]
 