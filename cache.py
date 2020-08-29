from cachetools import cached,TTLCache 

cache = TTLCache(maxsize=1, ttl=43200)