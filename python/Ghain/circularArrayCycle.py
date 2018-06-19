#Circular array with relative indiices has a complete cycle

import unittest
'''
if we have an input = [2,2,-1]
index 0 + value 2 = 2.
index 2 + value(-1) == 1
index 1 + value 2 == 3%3 = 0 
So onecomplete cycle
'''
def oneCycle(input):
    n = len(input)
    if n <2:
        return True
    indiices = 0
    i = 0
    while(indiices <= n):
        indiices += 1
        nextIndex = (i+input[i])%n
        print (nextIndex)
        if nextIndex == 0:
            break
        if indiices > n:
            break
        
        i = nextIndex
    
    print (indiices)   
    
    if indiices != n:
        return False
    return True
print (oneCycle([2,2,0]))        
    
def hasCycle(input):
    if len(input)<2:
        return True
    
    i = 0
    n = len(input)
    temp = {}
    while(i < n):
        j = input[i]
        if i not in temp:
            temp[i] = j
        else:
            break
        i = (i+j)%n
    
    if len(temp) != n:
        return False
    return True


print (hasCycle([2,2,0]))

class isCycleTests(unittest.TestCase):
    def isCycle1(self):
        #self.failUnless(hasCycle([2,2,-1]))
        self.assertEqual(hasCycle([2,2,-1]),True)
        
def main():
    unittest.main()

if __name__ == '__main__':
    print ('cool')
    main()        
        
        