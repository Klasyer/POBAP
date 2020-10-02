#lists for organazation purposuse 

#mods to change in items
known_mods = [
    {'mod':'ItemLvl', 'fix':'Item Level'},
    {'mod':'Name:', 'fix':''},
    {'mod':'Base:', 'fix':''}
] 

#mods to delete in items
mods_to_del = [
    'Crafted Item',
    'Implicits', 
    'LevelReq'
]

#mods to adds seperators after
seperetor_mods = [
    'Base',
    'Sockets',
    'ItemLvl', 
]

#special mods which require more than 1 seperator to be added after
special_seperator = [
    'Implicits'
]

#links to poeNinja, to be able to create the price list
poeNinja_links = [
    'https://poe.ninja/api/data/itemoverview?league=Heist&type=SkillGem&language=en',
    'https://poe.ninja/api/data/itemoverview?league=Heist&type=UniqueJewel&language=en',
    'https://poe.ninja/api/data/itemoverview?league=Heist&type=UniqueFlask&language=en',
    'https://poe.ninja/api/data/itemoverview?league=Heist&type=UniqueWeapon&language=en',
    'https://poe.ninja/api/data/itemoverview?league=Heist&type=UniqueArmour&language=en',
    'https://poe.ninja/api/data/itemoverview?league=Heist&type=UniqueAccessory&language=en'
]

#link for poeNinja to get the values of currencies
poeNinja_Currency = [
    'https://poe.ninja/api/data/currencyoverview?league=Heist&type=Currency&language=en'
]