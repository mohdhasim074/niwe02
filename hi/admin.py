from django.contrib import admin

# from .models import YourHindiModel# Import Hindi models here

class HindiAdminSite(admin.AdminSite):
    # admin.site.site_title = "एनआईडब्ल्यूई वेबसाइट"
    # admin.site.site_header = "एनआईडब्ल्यूई प्रबंधन"
    # admin.site.index_title = "एनआईडब्ल्यूई डैशबोर्ड"
    site_header = "एनआईडब्ल्यूई वेबसाइट"
    site_title = "एनआईडब्ल्यूई प्रबंधन"
    index_title = "एनआईडब्ल्यूई डैशबोर्ड"


hindi_admin_site = HindiAdminSite(name='hindi_admin')
# hindi_admin_site.register(YourHindiModel)  # Register Hindi models here
