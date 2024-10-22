from django.shortcuts import render, get_object_or_404
from .models import RightToInformation, Information, subInformation

def rti(request):

    rti = RightToInformation.objects.all().order_by('id')
    info= Information.objects.all().order_by('id')
    
    context = {
        'rti': rti, "info"  :info
                }
    return render(request, "rti.html", context)


def subInfo(request, info_id):
    item = get_object_or_404(Information, id=info_id)
    subInfo = subInformation.objects.filter(item=item).order_by('id')
  
    context = {
        "subInfo" : subInfo, "item": item
    }
    return render(request, "rti-sub.html", context)