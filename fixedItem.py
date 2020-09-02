from neededLists import * 
from helpFunctions import * 
import pobapi

class fixedItem: 
    def __init__(self, item): 
        self.oItem = item
        self.newItem = item
    
    def fix_sockets(self): 
        sockets_location = string_in_list('Sockets',self.newItem) 
        if sockets_location != -1: 
            sockets = self.newItem[sockets_location].replace('Sockets: ', '') 
            socket_list = [socket for socket in sockets]
            #for letter in socket_list: 


    
item = ['Rarity: Rare', 'Name: Eagle Paw', 'Base: Fingerless Silk Gloves', 'Crafted Item', 'Quality: 20', "Sockets: (('R', 'G', 'B', 'B'),)", 'LevelReq: 70', 'ItemLvl: 74', 'Implicits: 2', 'Trigger Word of Light when you take a Critical Strike', '16% increased Spell Damage', '+30 to Dexterity', '+40 to maximum Energy Shield', '35% increased Energy Shield', '+22 to maximum Life', '+42% to Lightning Resistance', '12% increased Attack Speed']

fi = fixedItem(item) 

print(fi.newItem)

print(fi.fix_sockets()) 