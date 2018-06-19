from abc import ABCMeta, abstractmethod

class IBehavior(metaclass = ABCMeta):
  @abstractmethod
  def run(self):
    pass

class ConcreteA(IBehavior):
  def run(self):
    return 'Mom'
    
class ConcreteB(IBehavior):
  def run(self,contractVal):
    return 'Dad'

class Client:
  cib = None
  
  def __init__(self,cib):
    self.cib = cib
  
  def execute(self):
    return self.cib.run()
    
#=====================================================================================================
class IRoyalty(metaclass = ABCMeta):
  @abstractmethod
  def royaltyCalc(self,pricePerBook,totalBooks):
    pass

class ConcreteRoyaltyA(IRoyalty):
  
  def royaltyCalc(self,pricePerBook,totalBooks):
    return (0.5 * pricePerBook * totalBooks)

class ConcreteRoyaltyB(IRoyalty):
    
  def royaltyCalc(self,pricePerBook,totalBooks):
    return (0.2 * pricePerBook * totalBooks)

    
class ATS:
  _iRoyalty = None
  
  def __init__(self,royaltyOption):
    self._iRoyalty = royaltyOption;
  
  def calculateRoyalty(self,pricePerBook,totalBooks):
    return self._iRoyalty.royaltyCalc(pricePerBook,totalBooks)
    

import unittest



'''
  crB = ConcreteRoyaltyB();
   crA = ConcreteRoyaltyA();
   ats = ATS(crB)
   ats.calculateRoyalty(20,100)
=> 400.0
   2000/400
=> 5.0
   ats = ATS(crA)
   ats.calculateRoyalty(20,100)
=> 1000.0
'''