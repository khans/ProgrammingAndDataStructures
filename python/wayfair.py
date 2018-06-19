import random

def say_hello():
    print('Hello, World')

for i in range(5):
    say_hello()

    

"""
    "3d6 + 2 - 2d8"
    "4d6 + 4d6 + 4d6"
    [4d6, 4d6,4d6]
    [+, +]
    [413d6,+,2,-,2d8]
    "- 2"
    
    returns int
"""

def read_dice_roll(expression):
    iList = expression.split(' ');
    #[3d6,+,2674,-,2d8]
    prevOperator = '+'
    totalSum = 0
    for each in iList:
        
        if 'd' in each:
            #divide it into parts , one before d and one after d
            tempSum = expand(each)    
            
            if prevOperator == '+':
                totalSum += tempSum
            else:
                totalSum -= tempSum
        
        elif len(each) == 1:
            if each == '+':
                prevOperator = '+'
            elif each == '-':
                prevOperator = '-'
            else:
                each = int(each)
                if prevOperator == '+':
                    totalSum += each
                else:
                    totalSum -= each
        
        else:
            each = int(each)
            if prevOperator == '+':
                totalSum += each
            else:
                totalSum -= each
            
    
    return totalSum

#evaluate an expression with d where n is the number of times the dice is rolled
def totalSum(n,end):
    sum = 0
    
    for i in range(n):
      
        sum += random.randint(1,end+1)
    return sum

# expand an expression with a symbol d
def expand(string):            #13d64
    subs1 = ''
    subs2 = ''
    for i in xrange(0,len(string)-1):
        if string[i] != 'd':
            subs1 += string[i]
        if string[i] == 'd':
            subs2 += string[i+1]
    subs1 = int(subs1)
    subs2 = int(subs2)
    
    tentativeSum = totalSum(subs1, subs2)
    return tentativeSum
                    
print(read_dice_roll('3d6 + 2 - 4d8'))    
    

    
