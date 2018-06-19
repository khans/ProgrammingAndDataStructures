import coin, player, coingame

def main():
    
    
    player1 = player.Player('Mark')
    player2 = player.Player('Tom')
    cg = coingame.CoinGame(player1,player2)
    
    cg.startGame()
    userAnswer = raw_input("Continue?")
    while(userAnswer[0] == 'Y' or userAnswer[0]=='y'):
        cg.startGame()
        userAnswer  = raw_input("Continue?")
    
        
    
if __name__ == "__main__":main()