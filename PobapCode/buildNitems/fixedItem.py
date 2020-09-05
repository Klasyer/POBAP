from PobapCode.needed.neededLists import special_seperator, seperetor_mods, mods_to_del, known_mods
from PobapCode.needed.helpFunctions import list_in_string, string_in_list, string_first_num, list_in_string_dict
import pobapi

class fixedItem: 
    def __init__(self, item): 
        self.oItem = item
        self.newItem = item

    def __setattr__(self,name, value): 
        if name == 'newItem' and not isinstance(value,list): 
            raise TypeError('The item has to be a list') 
        super().__setattr__(name, value)
    
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
    
    def fix_mods(self): 

        for i,mod in enumerate(self.newItem): 
            if list_in_string(mod, mods_to_del): 
                self.newItem[i] = 'Delete' 
            index = list_in_string_dict(mod, known_mods,'mod')
            if index != -1:  
                self.newItem[i] = self.newItem[i].replace(known_mods[index]['mod'],known_mods[index]['fix']).strip()
        self.newItem = list(filter(('Delete').__ne__,self.newItem))
        return True

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

