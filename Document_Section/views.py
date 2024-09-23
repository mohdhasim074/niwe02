from django.shortcuts import render
from django.http import request

from . models import Documents, Newsletters, RecordsRetentionSchedule, RevisedGuidelinesForProject, AnnualReport, FAQs, GeneralInformation, ComparisonBetweenFosilFuelAndWind, RelatedLinks


# documents
def download(request):
    documents = Documents.objects.all().order_by('id')
    if documents.exists():
       context = {'documents': documents}
       return render(request, "downloads.html", context)
    return render(request, "downloads.html")


# record retention
def record_retention(request):
    record = RecordsRetentionSchedule.objects.all().order_by('id')
    if record.exists():
        context = {'record': record}
        return render(request, "record_retention.html", context)
    return render(request, "record_retention.html")




# related links
def relatedlinks(request):

    relLinks = RelatedLinks.objects.all().order_by('id')
    if relLinks.exists():
        context = {'relLinks': relLinks}
        return render(request, 'relatedlinks.html', context)
    return render(request, "relatedlinks.html")

# general info
# def information_gi(request):
#     info = GeneralInformation.objects.all().order_by('id')
#     compare = ComparisonBetweenFosilFuelAndWind.objects.all().order_by('id')

    # if info.exists() and compare.exists():
#         context = {'info': info, 'compare': compare}
#         return render(request, "information_gi.html", context) 
#     return render(request, "information_gi.html")


# 
def information_gi(request):
    info = GeneralInformation.objects.all().order_by('id')
    if info.exists():
        context = {'info': info}
        return render(request, "information_gi.html", context) 
    return render(request, "information_gi.html")


# revised info
def information_hwed(request):
    revised = RevisedGuidelinesForProject.objects.all().order_by('id')
    if revised.exists():
        context = {'revised': revised}
        return render(request, "information_hwed.html", context)
    return render(request, "information_hwed.html")


# faqs
def faq(request):
    faqs = FAQs.objects.all().order_by('id')

    if faqs.exists():
        context = {'faqs': faqs}
        return render(request, "faq.html", context)
    return render(request, "faq.html")


# azadi
def azadi_ka_amrit_mahotsav(request):
    report = AnnualReport.objects.all().order_by('id')
    if report.exists():
        context = {'report': report}
        return render(request, "azadi_ka_amrit_mahotsav.html", context)
    return render(request, "azadi_ka_amrit_mahotsav.html")


#  power policy :
def wind_power_policy(request):
    return render (request, 'wind_power_policy.html')

