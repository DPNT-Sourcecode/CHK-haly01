

# noinspection PyUnusedLocal
# skus = unicode string

class items:
    def __init__(self, Item, Price):
        self.Item = Item
        self.Price = Price


class offItems(items):
    def __init__(self, Item, Price, sOffNum, sOffValue):
        super.__init__(Item, Price)
        self.sOffNum = sOffNum
        self.sOffValue = sOffValue

        
        
def checkout(skus):
    raise NotImplementedError()

