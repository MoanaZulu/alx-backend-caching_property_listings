from django.shortcuts import render

# Create your views here.



from django.shortcuts import render
from .utils import getallproperties

def property_list(request):
    properties = getallproperties()
    return render(request, 'properties/property_list.html', {'properties': properties})
