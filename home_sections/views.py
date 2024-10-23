from django.utils.translation import get_language

from django.shortcuts import render
from . models import *
# Create your views here.

def related_links(request):
    related_links =Related_links.objects.all()
    context={
        "related_links" : related_links
    }
    
    return render(request, "relatedlinks1.html", context)


def website_policy(request):
    return render (request, "web-policy.html")