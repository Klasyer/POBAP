from cachetools import cached,TTLCache 

PoeNinjaCache = TTLCache(maxsize=1, ttl=43200)

PriceCache = TTLCache(maxsize=250, ttl=43200)