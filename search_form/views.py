# views.py
from django.shortcuts import render
from about_section.models import AboutUs, DirectorGeneralMessage, Background, charter, OrganizationalChart, QualityPolicy
from Depart_Section.models import Departments
from certification_services.models import Certification_Procedure

from .forms import SearchForm

def search(request):
    form = SearchForm()
    # for about_section
    aboutUs = []
    background = []
    
    
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
            
            
            # Search in Department model
            departments = Departments.objects.filter(title__icontains=query) | Departments.objects.filter(description__icontains=query)

            # Search in Department model
            certification_procedures = Certification_Procedure.objects.filter(title__icontains=query) | Certification_Procedure.objects.filter(description__icontains=query)

    return render(request, 'search_results.html', {
        'form': form,
        # for about 
        'aboutUs': aboutUs,
        'background': background,
        #  for departments
        'departments': departments,
        'certification_procedures': certification_procedures,
    })
