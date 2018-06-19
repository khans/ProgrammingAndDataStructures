import random
class Card():
    suits = ['Spades',"Hearts","Clubs","Diamonds"]
    ranks = ['None','Ace','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        
    def show(self):
        print '{} of {}'.format(Card.ranks[self.rank],Card.suits[self.suit])
        # 3 of Hearts
    
    def __cmp__(self,other):
        c1 = (self.suit,self.rank) #tuples
        c2 = (other.suit,other.rank)
        return cmp(c1,c2)


class Deck():
    
    
    def __init__(self):
        self.cards = []
        self.build()
    
    def build(self):
        for s in range (4):
            for r in range (1,14):
                self.cards.append(Card(s,r))
    
    def show(self):
        for c in self.cards:
            c.show()
    
    def shuffle(self):
        '''for i in range(len(self.cards)-1,0,-1):
            r = random.randint(0,i)
            self.cards[i],self.cards[r]= self.cards[r],self.cards[i]
        '''
        random.shuffle(self.cards)
    
    def drawCard(self):
        return self.cards.pop()
        

class Player():
    def __init__(self,name):
        self.name = name
        self.hand = []
        
    def draw(self,deck):
        self.hand.append(deck.drawCard())
        return self #chain the calls
    
    def showHand(self):
        for card in self.hand:
            card.show()
            
    


d = Deck()
d.shuffle()

p = Player('Mark')
p.draw(d).draw(d).draw(d);
p.showHand()
                
        


        
    