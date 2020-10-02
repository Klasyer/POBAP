from cachetools import cached,TTLCache 

#just a bunch of cache to save some load times from things that might get repeated

PoeNinjaCache = TTLCache(maxsize=4, ttl=43200)

PriceCache = TTLCache(maxsize=250, ttl=43200)

CurrencyCache = TTLCache(maxsize=4, ttl=43200)

BuildCache = TTLCache(maxsize=500, ttl=3600)

PoePriceCache = TTLCache(maxsize=1000, ttl=3600)

ChaosCache = TTLCache(maxsize=10, ttl=43200)

FromChaosCache = TTLCache(maxsize=10, ttl=43200)