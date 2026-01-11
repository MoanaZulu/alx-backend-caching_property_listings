from django.core.cache import cache
from .models import Property

def getallproperties():
    # Try to get cached queryset
    properties = cache.get('allproperties')

    if properties is None:
        # Cache miss: fetch from DB
        properties = Property.objects.all()
        # Store in Redis for 1 hour (3600 seconds)
        cache.set('allproperties', properties, 3600)

    return properties
