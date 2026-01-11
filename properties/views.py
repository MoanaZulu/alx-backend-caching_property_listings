from django.shortcuts import render
from .utils import getallproperties

def property_list(request):
    properties = getallproperties()
    return render(request, 'properties/property_list.html', {'properties': properties})




from django.shortcuts import render
from .utils import get_all_properties

def property_list(request):
    properties = get_all_properties()
    return render(request, 'properties/property_list.html', {'properties': properties})



from django.http import JsonResponse
from django.views.decorators.cache import cache_page
from .models import Property

@cache_page(60 * 15)
def property_list(request):
    properties = list(Property.objects.values())
    return JsonResponse({
        "data": properties
    })
