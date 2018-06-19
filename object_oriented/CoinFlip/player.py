import random

class Player():
    
    coinOptions = ['head','tail']
    coinOption = ''
    
    def __init__(self,playername):
        self.name = playername
    
    def getCoinOption(self):
        return self.coinOption
    
    def getRandCoinOption(self):
        coinIndex = random.randint(0,1)
        self.coinOption = self.coinOptions[coinIndex] 
        return self.coinOptions[coinIndex]
    
    def setCoinOption(self,opponentOption):
        self.coinOption = self.coinOptions[0] if opponentOption is self.coinOptions[1] else self.coinOptions[1]
    
    def didPlayerWin(self,winningFlip):
        
        if self.coinOption == winningFlip:
            print "Player " + self.name + " won with a flip of " + self.coinOption
        else:
            print "Player " + self.name + " lost with a flip of " + self.coinOption
        
'''
player1 = Player('Mark')
player2 = Player('Tom')

#print player1.getRandCoinOption()   
player2.setCoinOption(player1.getRandCoinOption())
print player1.getCoinOption() 
print player2.getCoinOption() 
print player1.didPlayerWin('tail')

'''        
        
        