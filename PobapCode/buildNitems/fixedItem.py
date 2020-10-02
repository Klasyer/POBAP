from PobapCode.needed.neededLists import special_seperator, seperetor_mods, mods_to_del, known_mods
from PobapCode.needed.helpFunctions import list_in_string, string_in_list, string_first_num, list_in_string_dict
import pobapi

#A class for items to fixed thier text, to be able to pull from POB and price it, since poeprices requiers the format of poe 
#the overlays seem to get away with it by just copying the item from the game, but since it isnt an option, here i fix the items. 

class fixedItem: 
    def __init__(self, item): 
        self.oItem = item
        self.newItem = item

    def __setattr__(self,name, value): 
        if name == 'newItem' and not isinstance(value,list): 
            raise TypeError('The item has to be a list') 
        super().__setattr__(name, value)
    
#The sockets from pob come as a tuple, so text-wise it comes as (b,b),(g,g), this fixes it to be b-b g-g as in game

    def fix_sockets(self): 
        sockets_location = string_in_list('Sockets',self.newItem) 
        if sockets_location != -1: 
            sockets = self.newItem[sockets_location].replace('Sockets: ', '') 
            sockets = sockets.replace('), (','#')
            socket_list = [] 
            i = -1
            for socket in sockets: 
                if socket.isalpha():
                    if i > -1 and socket_list[i].isalpha(): 
                        socket_list.append('-')
                        i = i+1 
                    socket_list.append(socket)
                    i = i+1 
                elif socket == '#': 
                    socket_list.append(' ')
                    i = i+1 
            self.newItem[sockets_location] = 'Sockets: ' + ''.join(socket_list)
            return self.newItem[sockets_location]

#in Poe items, the items are seperated with dashes, between certain mod groups, come those seperators. 
#By keeping a list with those locaiton, it adds them to the item - in case of implicits, it adds a few lines to seperate it rightfuly 

    def add_seperetors(self): 
        fix = [] 
        seperate = '--------'
        repeater = 0

        for mod in self.newItem:
            if repeater > 0: 
                fix.append(seperate) 
                repeater = repeater - 1 
            fix.append(mod)
            if list_in_string(mod, special_seperator): 
                repeater = string_first_num(mod) + 1 
            elif list_in_string(mod, seperetor_mods):
                repeater = 1 

        self.newItem = fix 
        return fix
    
#this fixes the mods in the items word wise, deletes uneeded things from the lines and changes the differences 

    def fix_mods(self): 
        for i,mod in enumerate(self.newItem): 
            if list_in_string(mod, mods_to_del): 
                self.newItem[i] = 'Delete' 
            index = list_in_string_dict(mod, known_mods,'mod')
            if index != -1:  
                self.newItem[i] = self.newItem[i].replace(known_mods[index]['mod'],known_mods[index]['fix']).strip()
        self.newItem = list(filter(('Delete').__ne__,self.newItem))
        return True

#a finalized function that calls all the other functions

    def fix_item(self): 
        fixedItem.fix_sockets(self)
        fixedItem.add_seperetors(self)
        fixedItem.fix_mods(self)
        return True 
    
    def item_links(self): 
        sockets_location = string_in_list('Sockets',self.newItem) 
        maxSockets = 0                 
        if sockets_location != -1: 
            currentSockets = 1
            for letter in self.newItem[sockets_location].replace('Sockets: ', ''): 
                if letter == '-':
                    currentSockets = currentSockets+1
                if letter == ' ': 
                    maxSockets = max(maxSockets,currentSockets)
                    currentSockets = 1
            maxSockets = max(maxSockets,currentSockets)            
            if maxSockets < 5: 
                maxSockets = 0
        return maxSockets 

'''
item = ['Rarity: Rare', 'Name: Eagle Paw', 'Base: Fingerless Silk Gloves', 'Crafted Item', 'Quality: 20', "Sockets: (('R', 'G', 'B', 'B', 'W'),)", 'LevelReq: 70', 'ItemLvl: 74', 'Implicits: 2', 'Trigger Word of Light when you take a Critical Strike', '16% increased Spell Damage', '+30 to Dexterity', '+40 to maximum Energy Shield', '35% increased Energy Shield', '+22 to maximum Life', '+42% to Lightning Resistance', '12% increased Attack Speed']

#item = ['Rarity: Rare', 'Name: Eagle Paw', 'Base: Fingerless Silk Gloves', 'Crafted Item', 'Quality: 20', "Sockets: (('B', 'R'), ('B', 'G'), ('B', 'W'))", 'LevelReq: 70', 'ItemLvl: 74', 'Implicits: 2', 'Trigger Word of Light when you take a Critical Strike', '16% increased Spell Damage', '+30 to Dexterity', '+40 to maximum Energy Shield', '35% increased Energy Shield', '+22 to maximum Life', '+42% to Lightning Resistance', '12% increased Attack Speed']

#item = ['Rarity: Rare', 'Name: Eagle Paw', 'Base: Fingerless Silk Gloves', 'Crafted Item', 'Quality: 20',  'LevelReq: 70', 'ItemLvl: 74', 'Implicits: 2', 'Trigger Word of Light when you take a Critical Strike', '16% increased Spell Damage', '+30 to Dexterity', '+40 to maximum Energy Shield', '35% increased Energy Shield', '+22 to maximum Life', '+42% to Lightning Resistance', '12% increased Attack Speed']

fi = fixedItem(item) 


print(fi.newItem)

print(fi.fix_sockets()) 

print(fi.newItem)

print(fi.add_seperetors()) 

print(fi.newItem)

print(fi.fix_mods()) 

print(fi.newItem)

fi.fix_item() 

print(fi.newItem)

print(fi.item_links())
'''

