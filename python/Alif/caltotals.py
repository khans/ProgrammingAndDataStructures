'''
Write a method for a list input of the form: ['1','Z','X','+'],
such that when you see a number, it is a score is added to the last score
when you see'Z': you subtract the previous score from the total,
when you see 'X': you double the last score and add to total, when you see,
previous two scores will be added and that will be added to total
'''

class totals():
  def __init__(self,values):
    self.values = values
  def calcTotals(self):
    curr = 0; prev=0; dprev1 = 0; dprev2 = 0;
    sum = 0
    if len(self.values) > 0:
      for each in self.values:
        if (len(each) > 1): # for a number with more than 1 digit
          isNum = self.isValidInt(each)
          if isNum:
            curr =int(each)
          else:
            curr = 0
          dprev2 = dprev1;
          dprev1 = prev;
          prev = curr  
        else:
          if each == 'Z':
            curr = -curr;
            prev = dprev1;
            dprev1 = dprev2;
          elif each == 'X':
            curr = 2*prev
            dprev2 = dprev1;
            dprev1 = prev;
            prev = curr
          elif each == '+':
            curr = prev + dprev1
            dprev2 = dprev1;
            dprev1 = prev;
            prev = curr
          else:
            isNum = self.isValidInt(each)
            if isNum:
              curr = int(each)
            else:
              curr = 0
            dprev2 = dprev1;
            dprev1 = prev;
            prev = curr
        sum += curr     
      return sum  
            
      
      
  
  def isValidInt(self,string):
    valid = 1;
    for each in string:
      if ord(each) not in range (48,58):
        valid = 0;
        break
    return valid
        
p = totals(['55','4','3','Z','X','+']);
print(p.calcTotals())

          
    