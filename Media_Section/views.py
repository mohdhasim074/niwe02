from django.http import HttpResponse, request
from django.shortcuts import render, redirect, get_object_or_404
from .models import Award,  Events, Citizen_Charter, Gallery, SubGallery, Think_Tank,Sub_Think_Tank


# 
def awards(request):
    award = Award.objects.all().order_by('id')
    # if award.exists():
    return render(request, "awards.html", {'award':award})
# 
def events(request): 
    events = Events.objects.all().order_by('id')
    if events.exists():
        context = {'events': events}
    return render(request, "events.html", context)



def media(request):
     return render(request, "media.html")

# 
def charterHeader(request):
    charter = Citizen_Charter.objects.first()
    if charter:
        return HttpResponse(charter.document_File.url)

# gallery/sub-gallery


def album_list(request): 
    albums = Gallery.objects.all().order_by('serial')
    return render(request, 'gallery.html', {'albums': albums})


def sub_album_list(request, album_id):
    album = get_object_or_404(Gallery, id=album_id)
    sub_albums = SubGallery.objects.filter(album=album).order_by('id')
    return render(request, 'sub_gallery.html', {'album': album, 'sub_albums': sub_albums})


def think_tank(request):
    albums = Think_Tank.objects.all().order_by('id')
    context={
        "albums" : albums
    }
    return render (request, "think-tank.html", context)

def sub_think_tank(request, think_id):
    album = get_object_or_404(Think_Tank, id=think_id)
    sub_albums = Sub_Think_Tank.objects.filter(album=album).order_by('id')
    return render(request, 'sub_think.html', {'album': album, 'sub_albums': sub_albums})


