from django.http import HttpResponse, request
from django.shortcuts import render, redirect, get_object_or_404
from about_section.models import DirectorGeneralMessage
from Document_Section.models import WEG_Installation_Details_India, \
    weg_install_world_wise, AnnualReport, Newsletters

from Depart_Section.models import SDT_workshop, SDT_workshop_type, SDT_vayumitra, \
    SDT_InternationalTraining, SDT_National, \
    SDT_GlobalWindDay, SDT_Webinar, SDT_Customize_Training, SDT_Short_Term, \
    SDT_National_Page


def index(request):
    dgm = DirectorGeneralMessage.objects.all()
    if dgm.exists:
      return render(request, "index.html", {'dgm': dgm})


# sitemap
def sitemap(request):
    return render(request, 'sitemap.html')


def audit_report(request):
    return render(request, "audit_report.html")


def annual_account(request):
    return render(request, "annual_accounts.html")


def amrit_mahotsav_2021_22(request):
     return render(request, "amrit-mahotsav_2021-22.html")


def amrit_mahotsav_22_23(request):
    return render(request, "amrit-mahotsav-22-23.html")


def department_srra_online_training(request):
      return render(request, "department_srra_online_training.html")


def fowpi_report(request):
    return render(request, "fowpi_report.html")


def fowpi_workshop_presentation(request):
    return render(request, "fowpi_workshop_presentation.html")


def gallery(request):
    return render(request, "gallery.html")


def information_weg_installation(request):
    return render(request, "information_weg_installation.html")


def international_conference_wsra(request):
    return render(request, "international_conference_wsra.html")


def international_workshop_ppt(request):
    return render(request, "international_workshop_ppt.html")


def ireda_niwe_annual_awards(request):
    return render(request, "ireda_niwe_annual_awards.html")

# def media(request):
#     return render(request, "media.html")


def offshore_EPD_Gujarat(request):
    return render(request, "offshore_EPD_Gujarat.html")


def pan_india_workshop(request):
    return render(request, "pan-india_workshop.html")


def services(request):
    return render(request, "services.html")


def small_wind_energy_hybrid_system_presentation(request):
    return render(request, "small_wind_energy_&_hybrid_system_presentation.html")


def sub_gallery(request):
    return render(request, "sub-gallery.html")


def tenders(request):
    return render(request, "tenders.html")


def wind_potential(request):
    return render(request, "wind_potential.html")


def glossery(request):
    return render(request, "glossary.html")


def disclaimer(request):
    return render (request, "disclaimer.html")


def weg_install_country_wise(request):
    country_wise = weg_install_world_wise.objects.all()
    return render(request, "info_weg_install_details_country_wise.html", {'country_wise':country_wise})


def weg_install_India(request):
    details = WEG_Installation_Details_India.objects.all()
    return render(request, "info_weg_install_details_India.html", {'details': details})


# screen-reader-access
def Screen_Reader(request):
    return render(request, "screen-reader-access.html")

 
#  all side-tabs
def Academy(request):
    return render(request, 'tab-academic.html')


# library
def Library(request):
    return render (request, 'tab-library.html')




# 
def ITEC_training(request):
    return render (request, 'tab-ITEC.html')


def short_term_course(request):
    short = SDT_Short_Term.objects.all()
    context = {"short": short}
    return render (request, 'tab-short.html', context)


def customize_training(request):
    customize = SDT_Customize_Training.objects.all()
    return render (request, 'tab-customized.html', {"customize":customize})


def training_calander(request):
    return render (request, 'tab-calender.html')


def global_wind_day(request):
    globals = SDT_GlobalWindDay.objects.all()
    context = {"globals": globals}
    return render (request, 'tab-global.html', context)


def webinar(request):
    webinar = SDT_Webinar.objects.all()
    context = {"webinar": webinar}
    return render (request, 'tab-webinar.html', context)


# 
def offshore_lidar(request):
    return render (request, 'tab_offshore_lidar.html')


# 
def fowind_report(request):
    return render (request, 'tab-fowind_report.html')
# 

 
def workshop_confrence(request):
    workshop = SDT_workshop.objects.all()
    
    content = {"workshop": workshop}
    return render (request, 'tab-workshop.html', content)


def workshop_confrence_images(request, workshop_id):
   
    item = get_object_or_404(SDT_workshop, id=workshop_id)
    photos = SDT_workshop_type.objects.filter(item=item).order_by('id')
    content = {"item": item, "photos":photos}
    return render(request, "tab-workshop_photo.html", content)


# 
# 
def national_training(request):
    national = SDT_National.objects.all()
    return render (request, 'tab-national.html', {"national": national})


def national_training_data(request, data_id):
    item = get_object_or_404(SDT_National, id=data_id)
    national_data = SDT_National_Page.objects.filter(item=item).order_by('id')
    content = {"item": item, "national_data":national_data}
    return render(request, "tab-national-data.html", content)


def international_training(request):
    international = SDT_InternationalTraining.objects.all()
    content = {"international": international}
    return render (request, 'tab-international.html', content)


def international_training_eitec(request):
    # international = SDT_InternationalTraining.objects.all()
    # content = {"international": international}
    return render (request, 'tab-international-eitc.html', )


def international_training_sub_eitec(request):
    # international = SDT_InternationalTraining.objects.all()
    # content = {"international": international}
    return render (request, 'tab-international-sub-eitc.html',)

    
# 
def vayumitra_sdt(request):
    vayumitra = SDT_vayumitra.objects.all()
    content = {"vayumitra": vayumitra}
    return render (request, 'tab-vayumitra_sdt.html', content)


# 
# newsletters :
def newsletters(request):
    news = Newsletters.objects.all().order_by('id')
    if news.exists():
        context = {'news': news}
        return render (request, 'tab-news.html', context)
    return render (request, 'tab-news.html')


# annual_reports :
def annual_reports(request):
    annual = AnnualReport.objects.all().order_by('id')
    if annual.exists(): 
        context = {'annual': annual}
        return render (request, 'tab-annual.html', context)
    return render (request, 'tab-annual.html')

