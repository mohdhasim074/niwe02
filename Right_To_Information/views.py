from django.shortcuts import render
from .models import RightToInformation

def rti(request):

    rti = RightToInformation.objects.all().order_by('id')
    if rti.exists():
        context = {'rti': rti}
        return render(request, "rti.html", context)
    return render(request, "rti.html")