from django.http import HttpResponse, request
from django.shortcuts import render, redirect, get_object_or_404
from about_section.models import DirectorGeneralMessage
from Document_Section.models import WEG_Installation_Details_India, \
    weg_install_world_wise, AnnualReport, Newsletters

from Depart_Section.models import *

def hindi_index(request):
      return render(request, "hi_index.html")

# sitemap
def sitemap(request):
    return render(request, 'hi_sitemap.html')


def audit_report(request):
    return render(request, "hi_audit_report.html")


def annual_account(request):
    return render(request, "hi_annual_accounts.html")


def amrit_mahotsav_2021_22(request):
     return render(request, "hi_amrit-mahotsav_2021-22.html")


def amrit_mahotsav_22_23(request):
    return render(request, "hi_amrit-mahotsav-22-23.html")


def department_srra_online_training(request):
      return render(request, "hi_department_srra_online_training.html")


def fowpi_report(request):
    return render(request, "hi_fowpi_report.html")


def fowpi_workshop_presentation(request):
    return render(request, "hi_fowpi_workshop_presentation.html")


def gallery(request):
    return render(request, "hi_gallery.html")


def information_weg_installation(request):
    return render(request, "hi_information_weg_installation.html")


def international_conference_wsra(request):
    return render(request, "hi_international_conference_wsra.html")


def international_workshop_ppt(request):
    return render(request, "hi_international_workshop_ppt.html")


def ireda_niwe_annual_awards(request):
    return render(request, "hi_ireda_niwe_annual_awards.html")

# def media(request):
#     return render(request, "media.html")


def offshore_EPD_Gujarat(request):
    return render(request, "hi_offshore_EPD_Gujarat.html")


def pan_india_workshop(request):
    return render(request, "hi_pan-india_workshop.html")


def hi_services(request):
    return render(request, "hi_services.html")

 
def small_wind_energy_hybrid_system_presentation(request):
    return render(request, "hi_small_wind_energy_&_hybrid_system_presentation.html")


def sub_gallery(request):
    return render(request, "hi_sub-gallery.html")


def tenders(request):
    return render(request, "hi_tenders.html")


def wind_potential(request):
    return render(request, "hi_wind_potential.html")


def glossery(request):
    return render(request, "hi_glossary.html")


def disclaimer(request):
    return render (request, "hi_disclaimer.html")


def weg_install_country_wise(request):
    country_wise = weg_install_world_wise.objects.all()
    return render(request, "hi_info_weg_install_details_country_wise.html", {'country_wise':country_wise})


def weg_install_India(request):
    details = WEG_Installation_Details_India.objects.all()
    return render(request, "hi_info_weg_install_details_India.html", {'details': details})


# screen-reader-access
def Screen_Reader(request):
    return render(request, "hi_screen-reader-access.html")

 
#  all side-tabs
def Academy(request):
    return render(request, 'hi_tab-academic.html')


# library
def Library(request):
    Library = SDT_Library.objects.all()
    context = {
        "Library":Library
    }
    return render (request, 'hi_tab-library.html', context)


# 
def ITEC_training(request):
    return render (request, 'hi_tab-ITEC.html')


def ITEC_trainings(request):
    trainings = SDT_Eitc_Trainings.objects.all()
    context = {
        "trainings": trainings
    }
    return render (request, 'hi_tab-ITEC-training.html', context)


def ITEC_trainings_sub(request, training_id):
    item = get_object_or_404(SDT_Eitc_Trainings, id=training_id)
    sub_training = SDT_Eitc_Sub_Training.objects.filter(item=item).order_by('id')
    context = {
        "sub_training": sub_training, "item":item
    }
    return render (request, 'hi_tab-ITEC-training-sub.html', context)


def ITEC_training_countries(request):
    return render (request, 'hi_tab-ITEC-countries.html')


def ITEC_training_feedback(request):
    return render (request, 'hi_tab-ITEC-feedback.html')


def short_term_course(request):
    short = SDT_Short_Term.objects.all()
    context = {"short": short}
    return render (request, 'hi_tab-short.html', context)


def training_calander(request):
    national = SDT_Training_calender.objects.all()
    return render (request, 'hi_tab-calender.html', {"national": national})


def training_calander_sub(request, data_id):
    item = get_object_or_404(SDT_Training_calender, id=data_id)
    national_data = SDT_Training_Sub_calender.objects.filter(item=item).order_by('id')
    content = {"item": item, "national_data":national_data}
    return render(request, "hi_tab-calender-sub.html", content)


def global_wind_day(request):
    globals = SDT_GlobalWindDay.objects.all()
    context = {"globals": globals}
    return render (request, 'hi_tab-global.html', context)

def gloabl_sub_wind_day(request, global_id):
    item=get_object_or_404(SDT_GlobalWindDay, id=global_id)
    sub_global = SDT_Global_Sub_Wind.objects.filter(item=item).order_by('id')
    context={
        "sub_global":sub_global, "item":item
    }
    return render (request, 'hi_tab-global-sub.html', context)


def webinar(request):
    webinar = SDT_Webinar.objects.all()
    context = {"webinar": webinar}
    return render (request, 'hi_tab-webinar.html', context)


# 
def offshore_lidar(request):
    return render (request, 'hi_tab_offshore_lidar.html')


# 
def fowind_report(request):
    return render (request, 'hi_tab-fowind_report.html')
# 

 
def workshop_confrence(request):
    workshop = SDT_workshop.objects.all()
    
    content = {"workshop": workshop}
    return render (request, 'hi_tab-workshop.html', content)


def workshop_confrence_images(request, workshop_id):
   
    item = get_object_or_404(SDT_workshop, id=workshop_id)
    photos = SDT_workshop_type.objects.filter(item=item).order_by('id')
    content = {"item": item, "photos":photos}
    return render(request, "hi_tab-workshop_photo.html", content)


def customize_training(request):
    customize = SDT_Customize_Training.objects.all()
    return render (request, 'hi_tab-customized.html', {"customize":customize})


def customize_training_sub(request, id):
    item = get_object_or_404(SDT_Customize_Training, id=id)
    custom = SDT_Customize_Training_Sub.objects.filter(item=item).order_by('id')
    content = {"item": item, "custom":custom}
    return render(request, "hi_tab-customized_sub.html", content)


# 
# 
def national_training(request):
    national = SDT_National.objects.all()
    return render (request, 'hi_tab-national.html', {"national": national})


def national_training_data(request, data_id):
    item = get_object_or_404(SDT_National, id=data_id)
    national_data = SDT_National_Page.objects.filter(item=item).order_by('id')
    content = {"item": item, "national_data":national_data}
    return render(request, "hi_tab-national-data.html", content)


def training_list(request):
    trainings = SDT_InternationalTraining.objects.all()
    return render(request, 'hi_tab-international.html', {'trainings': trainings})


def eitec_detail(request, training_slug):
    training = get_object_or_404(SDT_InternationalTraining, slug=training_slug)
    eitecs = SDT_InternationalTraining_eitec.objects.filter(item=training)
    return render(request, 'hi_tab-international-eitc.html', {'training': training, 'eitecs': eitecs})


def sub_eitec_detail(request, eitec_slug):
    eitec = get_object_or_404(SDT_InternationalTraining_eitec, slug=eitec_slug)
    sub_eitecs = SDT_InternationalTraining_sub_eitec.objects.filter(eitec=eitec)
    return render(request, 'hi_tab-international-sub-eitc.html', {'eitec': eitec, 'sub_eitecs': sub_eitecs})


# 
def vayumitra_sdt(request):
    vayumitra = SDT_vayumitra.objects.all()
    content = {"vayumitra": vayumitra}
    return render (request, 'hi_tab-vayumitra_sdt.html', content)

# # newsletters :
def newsletters(request):
    news = Newsletters.objects.all().order_by('-id')
    context = {'news': news}
    return render (request, 'hi_tab-news.html', context)

# annual_reports :
def annual_reports(request):
    annual = AnnualReport.objects.all().order_by('-id') 
    context = {'annual': annual}
    return render (request, 'hi_tab-annual.html', context)

def Events(request):
    return render (request, "hi_events.html")

def whatsNew(request):
    return render (request, "hi_whats_new.html")

def mnreNew(request): 
    return render (request, "hi_mnre_new.html")


def corporate_film_hindi(request):
    return render(request, 'hi_corporate_film.html')
