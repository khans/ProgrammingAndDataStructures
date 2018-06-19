
import random

class Coin():
    coinOptions = ['head','tail']
    coinOption = ''
    
    def __init__(self):
        coinIndex = random.randint(0,1)
        self.coinOption = self.coinOptions[coinIndex]
        
    def getCoinOption(self):
        return self.coinOption

'''coin1 = Coin()
print coin1.getCoinOption()
'''