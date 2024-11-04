from django.shortcuts import render, get_object_or_404
from .models import RightToInformation, Information, subInformation

def rti(request):

    rtis = RightToInformation.objects.all().order_by('id')
    info= Information.objects.all().order_by('id')
    
    context = {
        'rtis': rtis, "info"  :info
                }
    return render(request, "Right_To_Information/hi_rti.html", context)


def subInfo(request, info_id):
    item = get_object_or_404(Information, id=info_id)
    subInfo = subInformation.objects.filter(item=item).order_by('id')
  
    context = {
        "subInfo" : subInfo, "item": item
    }
    return render(request, "hi_rti-sub.html", context)