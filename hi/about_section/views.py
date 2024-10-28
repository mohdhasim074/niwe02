from django.shortcuts import render, redirect
from django.http import HttpRequest
from .models import AboutUs, DirectorGeneralMessage, Background, charter, OrganizationalChart, QualityPolicy

# about us
def hi_about_us(request):
    aboutUs = AboutUs.objects.all()
    content = {'aboutUs': aboutUs}
    return render(request, "about_section/hi_about_us.html", content)

# background
def hi_about_background(request):
    background = Background.objects.all()
    content = {'background': background}
    return render(request, "about_section/hi_about_background.html", content)

# charter
def hi_about_charter(request):
    chart = charter.objects.all()
    content = {'chart': chart}
    return render(request, "about_section/hi_about_charter.html", content)
# dgm
def hi_about_dgm(request):
    dgm = DirectorGeneralMessage.objects.all()
    content = {'dgm': dgm}
    return render(request, "about_section/hi_about_dgm.html", content)

# organisation
def hi_about_org(request):
    org = OrganizationalChart.objects.all()
    content = {'org': org}
    return render(request, "about_section/hi_about_org.html", content)

# quality
def hi_about_qlty_ply(request):

    quality = QualityPolicy.objects.all()
    content = {'quality': quality}
    return render(request, "about_section/hi_about_qlty_ply.html", content)

#  staff-profile

