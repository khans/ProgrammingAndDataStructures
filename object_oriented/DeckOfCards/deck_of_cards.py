import random

class Card(object):
    suit_names = ["Clubs","Diamonds","Hearts","Spades"]
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', 
              '8', '9', '10', 'Jack', 'Queen', 'King']
    def __init__(self,suit = 0, rank = 2):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return '%s of %s'% (Card.rank_names[self.rank],Card.suit_names[self.suit])
    
    def __cmp__(self,other):
        t1 = (self.suit,self.rank)
        t2= (other.suit, other.rank)
        return cmp(t1,t2)


card1 = Card(1,4)  #(suit,rank)
#print card1.__str__()

card2 = Card(1,4)
#print card2.__str__()

print card1.__cmp__(card2)



#Deck of Cards
class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit,rank)
                self.cards.append(card)
    def __str__(self):
        res = [str(card) for card in self.cards]
        return '\n'.join(res) 
    
    def add_card(self,card):
        return self.cards.append(card)
    
    def pop_card(self):
        return self.cards.pop()
    
    def shuffle(self):
        return random.shuffle(self.cards)
    

deck = Deck()
#print deck


