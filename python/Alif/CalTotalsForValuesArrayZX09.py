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
    values = self.values
    print (values);
    currScore = 0
    lastScore = 0
    scoresArr = [0,0,0]
    totalScore = 0
    
    if len(values) > 0:
      for each in values:
        if (len(each) > 1): # for a number with more than 1 digit
          isNum = self.isValidInt(each)
          if isNum:
            currScore = int(each)
          else:
            currScore = 0
            
          lastScore = currScore  
          totalScore += currScore
          scoresArr.append(lastScore)
        else:
          if each == 'Z':
            totalScore -= scoresArr[-1]
            scoresArr.pop()
            lastScore = scoresArr[-1]
          elif each == 'X':
            currScore = 2*lastScore
            totalScore += currScore
            lastScore = currScore
            scoresArr.append(lastScore)
          elif each == '+':
            if len(scoresArr) > 1:
              currScore = scoresArr[-1]+scoresArr[-2]
            if len(scoresArr) == 1:
              currScore = scoresArr[-1] + 0
            else:
              currScore = 0
            lastScore = currScore
            totalScore += currScore
            scoresArr.append(lastScore)
          else:
            isNum = self.isValidInt(each)
            if isNum:
              currScore = int(each)
            else:
              currScore = 0
            
            lastScore = currScore  
            totalScore += currScore
            scoresArr.append(lastScore) 
      #while(scoresArr):
      #  scoresArr.pop()
      print (scoresArr)
      return totalScore
  def isValidInt(self,string):
    valid = 1;
    for each in string:
      if ord(each) not in range (48,58):
        valid = 0;
        break
    return valid
        
p = totals(['55','4','3','Z','X']);
print(p.calcTotals())

          
    