from django.shortcuts import render
from . models import *
# Create your views here.

def related_links(request):
    related_links =Related_links.objects.all()
    context={
        "related_links" : related_links
    }
    
    return render(request, "relatedlinks1.html", context)