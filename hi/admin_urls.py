from django.urls import path
from .admin import hindi_admin_site

urlpatterns = [
    path('hi/', hindi_admin_site.urls),
]
