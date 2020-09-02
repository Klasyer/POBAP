import pobapi 
from neededLists import * 

class fixedBuild: 
    def __init__(self, url): 
        self.originalBuild = pobapi.from_url(url)
        item_list = []
        for i in range(len(self.originalBuild.items)): 
            item_list.append(str(self.originalBuild.items[i]))

        self.FixedItems = []
        for item in item_list: 
            self.FixedItems.append(item.splitlines())

    def fix_sockets(self):
        return 'fuck'

b1 = fixedBuild("https://pastebin.com/UfSV0JNU")

print(b1.fix_sockets()) 