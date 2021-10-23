

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

class pItems(items):
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

class selItems(items):
    def __init__(self, Item, Price, sOffNum, sOffNumFree):
        super().__init__(Item, Price)
        self.sOffNum = sOffNum
        self.sOffNumFree = sOffNumFree

    def tPrice(self, iNumber, _):
        if iNumber%(self.sOffNum+self.sOffNumFree) == 0:
            return int(iNumber/(self.sOffNum+self.sOffNumFree))*self.sOffNum * self.Price
        else:
            return (int(iNumber/(self.sOffNum+self.sOffNumFree))*self.sOffNum + iNumber%(self.sOffNum+self.sOffNumFree)) * self.Price

class sItems(items):
    def __init__(self, Item, Price, sOffNum, freeItem, freeItemNum):
        super().__init__(Item, Price)
        self.sOffNum = sOffNum
        self.freeItem = freeItem
        self.freeItemNum = freeItemNum

    def tPrice(self, iNumber, fBasket):
        sPrice = iNumber*self.Price
        if isinstance(self.freeItem, offItems) or isinstance(self.freeItem, selItems) or isinstance(self.freeItem, multiOffItems):
            discount = self.freeItem.tPrice(fBasket.count(self.freeItem.Item), fBasket) - self.freeItem.tPrice(fBasket.count(self.freeItem.Item)-int(iNumber/self.sOffNum), fBasket)        
        else:
            discount = (int(iNumber/self.sOffNum)* self.freeItem.Price
            if int(iNumber/self.sOffNum)*self.freeItemNum < fBasket.count(self.freeItem.Item)
            else fBasket.count(self.freeItem.Item)*self.freeItem.Price)
        if discount<0:
            discount=0
        
        return sPrice-discount
    
def checkout(skus):
    itA = multiOffItems('A', 50, 3, 130, 5, 200)
    itB = offItems('B', 30, 2, 45)
    itC = items('C', 20)
    itD = items('D', 15)
    itE = sItems('E', 40, 2, itB, 1)
    itF = selItems('F', 10, 2, 1)
    itG = items('G', 20)
    itH = multiOffItems('H', 10, 5, 45, 10, 80)
    itI = items('I', 35)
    itJ = items('J', 60)
    itK = offItems('K', 80, 2, 150)
    itL = items('L', 90)
    itM = items('M', 15)
    itN = sItems('N', 40, 3, itM, 1)
    itO = items('O', 10)
    itP = offItems('P', 50, 5, 200)
    itQ = offItems('Q', 30, 3, 80)
    itR = sItems('R', 50, 3, itQ, 1)
    itS = items('S', 30)
    itT = items('T', 20)
    itU = selItems('U', 40, 3, 1)
    itV = multiOffItems('V', 50, 2, 90, 3, 130)
    itW = items('W', 20)
    itX = items('X', 90)
    itY = items('Y', 10)
    itZ = items('Z', 50)

    
    itList = [itA, itB, itC, itD, itE, itF, itG, itH, itI, itJ, itK, itL, itM, itN, itO, itP, itQ, itR, itS, itT, itU, itV, itW, itX, itY, itZ]
    try:
        basket=[vals for vals in skus]
        uItems = set(basket)
        basPrices=[]
        for i in uItems:
            basPrices.append([x.tPrice(basket.count(i), basket) for x in itList if x.Item == i][0])
        return sum(basPrices)
    except:
        return -1
