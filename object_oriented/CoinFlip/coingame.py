import random
import coin, player

class CoinGame():
    players = []
    coin = coin.Coin()
    
    def __init__(self,player1,player2):
        self.players.append(player1)
        self.players.append(player2)
    
    def startGame(self):
        for each in self.players:
            print each.name
        pIndex = random.randint(0,1)
        print 'playerIndex is '+ str(pIndex)
        playersPick = self.players[pIndex].getRandCoinOption()
        print 'playersPick is '+ playersPick
        
        opponentIndex = 0 if pIndex is 1 else 1
        self.players[opponentIndex].setCoinOption(playersPick)
        
        winningFlip = self.coin.getCoinOption()
        print 'winningFlip is ' + winningFlip
        
        for each in self.players:
             each.didPlayerWin(winningFlip)
        
        
'''
player1 = player.Player('Mark')
player2 = player.Player('Tom')
print player1.getRandCoinOption() 
print player1.getCoinOption()
player2.setCoinOption(player1.getCoinOption())
print player2.getCoinOption()

cg = CoinGame(player1,player2)
print '----------------------'
cg.startGame()   

'''       
        
    