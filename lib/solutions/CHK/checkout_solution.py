

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
        super.__init__(Item, Price)
        self.sOffNum = sOffNum
        self.sOffValue = sOffValue

    def tPrice(self, iNumber):
        return self.sOffValue*int(iNumber/self.sOffNum) + (iNumber%self.sOffNum)*self.Price
    
    


        
        
def checkout(skus):
    raise NotImplementedError()


