from cachetools import cached,TTLCache 

PoeNinjaCache = TTLCache(maxsize=1, ttl=43200)