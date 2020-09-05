from cachetools import cached,TTLCache 

PoeNinjaCache = TTLCache(maxsize=4, ttl=43200)

PriceCache = TTLCache(maxsize=250, ttl=43200)

CurrencyCache = TTLCache(maxsize=4, ttl=43200)