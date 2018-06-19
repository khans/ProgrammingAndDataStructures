class Fraction:
  def __init__(self,num,den,love):
    assert type(num) == int and type(den)==int
    self.num = num
    self.den = den
    assert type(love) == str
    self.love = love
  
  def __str__(self):
    return str(self.num)+"/"+str(self.den) + self.love
      
    
    
f = Fraction(3,4,90)
print(f)