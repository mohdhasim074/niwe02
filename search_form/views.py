# views.py
from django.shortcuts import render
from about_section.models import AboutUs, DirectorGeneralMessage, Background, charter, OrganizationalChart, QualityPolicy
from Depart_Section.models import Departments
from certification_services.models import Certification_Procedure
from Media_Section.models import Award, Citizen_Charter, Events, Gallery, Think_Tank
from .forms import SearchForm

def search(request):
    form = SearchForm()
    # for about_section
    aboutUs = []
    background = []
    DGMessage= []
    charters= []
    OrgChart = []
    qualityPolicy=[]
    
    #  for media section
    award = []
    citizen_charter= []
    events= []
    gallery= []
    thin_tank= []
    
    # for department_sections
    departments = [] 
    certification_procedure = []

    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            # Search in About_section models
            aboutUs = AboutUs.objects.filter(title__icontains=query) | AboutUs.objects.filter(description__icontains=query)
            background = Background.objects.filter(description__icontains=query)
            DGMessage =DirectorGeneralMessage.objects.filter(title__icontains=query) | DirectorGeneralMessage.objects.filter(description__icontains=query) | DirectorGeneralMessage.objects.filter(Dirs_image__icontains=query)  
            charters  = charter.objects.filter(preamble__icontains=query) | charter.objects.filter(mission__icontains=query) | charter.objects.filter(objectives__icontains=query)
            OrgChart = OrganizationalChart.objects.filter(description__icontains=query) | OrganizationalChart.objects.filter(image__icontains=query)
            qualityPolicy =   QualityPolicy.objects.filter(policyImage__icontains=query)


            # Search in media_section models
            
            
            # Search in Department model
            departments = Departments.objects.filter(title__icontains=query) | Departments.objects.filter(description__icontains=query)

            # Search in Department model
            certification_procedure = Certification_Procedure.objects.filter(title__icontains=query) | Certification_Procedure.objects.filter(description__icontains=query)

    return render(request, 'search_results.html', {
        'form': form,
        # for about 
        'aboutUs': aboutUs,
        'background': background,
        'DGMessage' : DGMessage,
        'charters': charters,
        'OrgChart' : OrgChart, 
        'qualityPolicy' : qualityPolicy,
        #  for departments
        'departments': departments,
        'certification_procedure': certification_procedure,
    })
