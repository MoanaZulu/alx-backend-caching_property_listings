from django.core.cache import cache
from .models import Property

def getallproperties():
    properties = cache.get('allproperties')
    if properties is None:
        properties = Property.objects.all()
        cache.set('allproperties', properties, 3600)
    return properties



import logging
from django_redis import get_redis_connection

logger = logging.getLogger(__name__)

def get_redis_cache_metrics():
    try:
        # Connect to Redis
        conn = get_redis_connection("default")
        info = conn.info()

        # Retrieve hits and misses
        keyspace_hits = info.get("keyspace_hits", 0)
        keyspace_misses = info.get("keyspace_misses", 0)

        # Calculate totals and hit ratio
        total_requests = keyspace_hits + keyspace_misses
        hit_ratio = (keyspace_hits / total_requests) if total_requests > 0 else 0

        # Log metrics
        logger.info(f"Redis cache metrics - Hits: {keyspace_hits}, Misses: {keyspace_misses}, Hit Ratio: {hit_ratio}")

        return {
            "keyspace_hits": keyspace_hits,
            "keyspace_misses": keyspace_misses,
            "hit_ratio": hit_ratio,
        }

    except Exception as e:
        logger.error(f"Error retrieving Redis cache metrics: {e}")
        return {
            "keyspace_hits": 0,
            "keyspace_misses": 0,
            "hit_ratio": 0,
        }
