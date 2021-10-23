

# noinspection PyUnusedLocal
# skus = unicode string

class items:
    def __init__(self, Item, Price):
        self.Item = Item
        self.Price = Price
    
    def tPrice(self, iNumber):
        return self.Price * iNumber


class offItems(items):
    def __init__(self, Item, Price, sOffNum, sOffValue):
        super().__init__(Item, Price)
        self.sOffNum = sOffNum
        self.sOffValue = sOffValue

    def tPrice(self, iNumber):
        return self.sOffValue*int(iNumber/self.sOffNum) + (iNumber%self.sOffNum)*self.Price


class sItems(items):
    def __init__(self, Item, Price, sOffNum, freeItem, freeItemNum):
        super().__init__(Item, Price)
        self.sOffNum = sOffNum
        self.freeItem = freeItem
        self.freeItemNum = freeItemNum

    def tPrice(self, iNumber):
        return self.sOffValue*int(iNumber/self.sOffNum) + (iNumber%self.sOffNum)*self.Price

def checkout(skus):
    itList = [offItems('A', 50, 3, 130), offItems('B', 30, 2, 45), items('C', 20), items('D', 15)]
    try:
        basket=[vals for vals in skus]
        uItems = set(basket)
        basPrices=[]
        for i in uItems:
            basPrices.append([x.tPrice(basket.count(i)) for x in itList if x.Item == i][0])
        
        return sum(basPrices)
    except:
        return -1


