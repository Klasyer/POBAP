import pobapi 
from PobapCode.buildNitems.fixedItem import fixedItem

class fixedBuild: 
    def __init__(self, build): 
        if 'pastebin.com' in str(build): 
            self.originalBuild = pobapi.from_url(build)
        else:
            self.originalBuild = pobapi.from_import_code(build)
        item_list = []
        for i in range(len(self.originalBuild.items)): 
            item_list.append(str(self.originalBuild.items[i]))

        self.buildItems = []
        for item in item_list: 
            self.buildItems.append(item.splitlines())

    def fix_items(self):
        for i,item in enumerate(self.buildItems):
            Fixitem = fixedItem(item) 
            Fixitem.fix_item()
            self.buildItems[i] = Fixitem.newItem

        return True
            
'''
b1 = fixedBuild("https://pastebin.com/UfSV0JNU")

for item in b1.buildItems: 
    print(item)
    print('###########')

b1.fix_items()

for item in b1.buildItems: 
    print(item)
    print('###########')
'''