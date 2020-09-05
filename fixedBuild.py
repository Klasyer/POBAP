import pobapi 
from neededLists import * 
from fixedItem import fixedItem 

class fixedBuild: 
    def __init__(self, url): 
        self.originalBuild = pobapi.from_url(url)
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
            

b1 = fixedBuild("https://pastebin.com/UfSV0JNU")

for item in b1.buildItems: 
    print(item)
    print('###########')

b1.fix_non_uniques()

for item in b1.buildItems: 
    print(item)
    print('###########')