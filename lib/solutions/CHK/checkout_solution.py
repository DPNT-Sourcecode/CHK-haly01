

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
        
def checkout(skus):
    itA = offItems('A', 50, 3, 130)
    itB = offItems('B', 30, 2, 45)
    itC = items('C', 20)
    itD = items('D', 15)

    print([vals.upper() for vals in skus])
    
checkout('ab')



