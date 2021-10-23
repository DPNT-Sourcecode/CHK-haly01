

# noinspection PyUnusedLocal
# skus = unicode string

class items:
    def __init__(self, Item, Price):
        self.Item = Item
        self.Price = Price
    
    def tPrice(self, iNumber, _):
        return self.Price * iNumber


class offItems(items):
    def __init__(self, Item, Price, sOffNum, sOffValue):
        super().__init__(Item, Price)
        self.sOffNum = sOffNum
        self.sOffValue = sOffValue

    def tPrice(self, iNumber, _):
        return self.sOffValue*int(iNumber/self.sOffNum) + (iNumber%self.sOffNum)*self.Price

class multiOffItems(items):
    def __init__(self, Item, Price, sOffNum, sOffValue, lOffNum, lOffValue):
        super().__init__(Item, Price)
        self.sOffNum = sOffNum
        self.sOffValue = sOffValue
        self.lOffNum = lOffNum
        self.lOffValue = lOffValue

    def tPrice(self, iNumber, _):
        return self.lOffValue*int(iNumber/self.lOffNum) + self.sOffValue*int(iNumber%self.lOffNum/self.sOffNum) + (int(iNumber%self.lOffNum)%self.sOffNum)*self.Price


class sItems(items):
    def __init__(self, Item, Price, sOffNum, freeItem, freeItemNum):
        super().__init__(Item, Price)
        self.sOffNum = sOffNum
        self.freeItem = freeItem
        self.freeItemNum = freeItemNum

    def tPrice(self, iNumber, fBasket):
        sPrice = iNumber*self.Price
        discount = (self.freeItem.sOffValue*int(int(iNumber/self.sOffNum)/self.freeItem.sOffNum) + 
        (int(iNumber/self.sOffNum)%self.freeItem.sOffNum)*(self.freeItem.Price*self.freeItem.sOffNum - self.freeItem.sOffValue)         
        if int(iNumber/self.sOffNum)*self.freeItemNum <= fBasket.count(self.freeItem.Item)
        else self.freeItem.sOffValue*int(fBasket.count(self.freeItem.Item)/self.freeItem.sOffNum) + 
        (fBasket.count(self.freeItem.Item)%self.freeItem.sOffNum)*self.freeItem.Price)

        return sPrice-discount

def checkout(skus):
    itA = multiOffItems('A', 50, 3, 130, 5, 200)
    itB = offItems('B', 30, 2, 45)
    itC = items('C', 20)
    itD = items('D', 15)
    itE = sItems('E', 40, 2, itB, 1)
    
    itList = [itA, itB, itC, itD, itE]
    try:
        basket=[vals for vals in skus]
        uItems = set(basket)
        basPrices=[]
        for i in uItems:
            basPrices.append([x.tPrice(basket.count(i), basket) for x in itList if x.Item == i][0])
        return sum(basPrices)
    except Exception as e:
        return e

print(checkout('AAAAABBEED'))
