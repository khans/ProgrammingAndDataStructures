import sys

class Heap():
  capacity = 10
  size = 0
  items = []
  
  def getleftchildindex(self,parentIndex):
    return (2*parentIndex + 1)
  def getrightchildindex(self, parentIndex):
    return (2*parentIndex+2)
  def getParentIndex(self, childIndex):
    return ((childIndex - 1)//2)
  
  def hasleftchild(self,index):
    return (self.getleftchildindex(index) < self.size)
  def hasrightchild(self,index):
    return (self.getrightchildindex(index) < self.size)
  def hasparent(self,index):
    return (self.getParentIndex(index)>=0)
    
  def leftchildvalue(self,index):
    return self.items[self.getleftchildindex(index)]
  def rightchildvalue(self,index):
    return self.items[self.getrightchildindex(index)]
  def parentvalue(self,index):
    return self.items[self.getParentIndex(index)]  
  
  def swap(self,a,b):
    temp = a; a = b; b = temp;
    return
  
  def ensureExtraCapacity(self):
    if self.size == self.capacity:
      self.capacity *= 2
  
  def peek(self):
    try: 
      if self.size > 0:
        return self.items[0]
    except:
      e = sys.exc_info()[0]
      print ("Error is %s"%e)
    
  def poll(self):
    try:
      if self.size > 0:
        item = self.items[0]
        self.items[0] = self.items[self.size - 1]
        self.items.pop()
        self.size -= 1
        self.heapifyDown()
        return item
    except:
      e = sys.exc_info()[0]
      print ("Error is %s"%e)
  
  def addItem(self, item):
    self.ensureExtraCapacity()
    self.items.append(item)
    self.size += 1
    self.heapifyUp()
    return

  def heapifyDown(self):
    index = 0;
    while (self.hasleftchild(index)):
      print (index)
      smallerChildIndex = self.getleftchildindex(index)
      if (self.hasrightchild(index) and self.rightchildvalue(index) < self.leftchildvalue(index)):
        print ('yes')
        smallerChildIndex = self.getrightchildindex(index)
      print (smallerChildIndex)
      print (self.items[index])
      print (self.items[smallerChildIndex])
      if (self.items[index] < self.items[smallerChildIndex]):
        break
      else:
        self.items[index], self.items[smallerChildIndex] = self.items[smallerChildIndex], self.items[index]
      
      index = smallerChildIndex
  
 
  def heapifyUp(self):
    index = self.size - 1
    while(self.hasparent(index) and self.parentvalue(index)>self.items[index]):
      self.swap(self.getParentIndex(index),index)
      index = self.getParentIndex(index)
      
  
  def seeItems(self):
    for each in self.items:
      print (each)
  
  def seeSize(self):
    return self.size