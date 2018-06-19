
from collections import deque,defaultdict
class Table:
  capacity = 0
  availability = True
  occupancy = 0
  
  def __init__(self,number):
    self.number = number
  
  def addOccupant(self):
    self.occupancy += 1
    self.availability = False
  
  def setCapacity(self,capacity):
    self.capacity = capacity


  def getTableNumber(self):
    return self.number
    

class Order:
  def __init__(self):
    self.orderList = {}
    
  def addOrder(self,item,count):
    self.orderList[item] = count
    
  
  

class Kitchen:
  queue = deque();
  free = False
  
  def make(self,order):
    self.queue.append(order)
      
    
  def isReady(self,order):
    if order in self.queue:
      return False
    else:
      return True
  
  def getFood(self):
    self.queue.popleft();
    
  def getQueue(self):
    return self.queue;
  
  def doneDish(self):
    self.queue.popleft()
    
    
