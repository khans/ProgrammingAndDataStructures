#https://www.youtube.com/watch?v=XKu_SEDAykw

class Result():
    def __init__(self):
        self.found = False
        self.pair = [-1,-1]
    
class Solution():
    #Solution 1: Sorted List
    def foundPairToSum(self,inputList, total):
        if len(inputList) < 2:
            raise IndexError('Sum needs atleast two elements')
        res = Result();
        former = 0; latter = len(inputList)-1
        
        while(former < latter):
            sum = inputList[former] + inputList[latter]
            if sum == total:
                res.found = True
                res.pair[0] = former
                res.pair[1] = latter
                return res
            if sum > total:
                latter -= 1
            else:
                former += 1
        return res
    #Solution 1: Sorted List
    def fPTS(self,inputList, total):
        comp = set();
        for each in inputList:
            c = total-each
            if each in comp:
                print(comp)
                return True
            comp.add(c)
        print (comp)
        return False
        
        
            
        
s = Solution()
input = [1,2,3,9]
print(s.foundPairToSum(input,8).found)
print(s.foundPairToSum(input,8).pair)
input = [1,2,4,4]
print(s.foundPairToSum(input,8).found)
print(s.foundPairToSum(input,8).pair)
input = [ -1, 0, 4, 4, 9]
print(s.foundPairToSum(input,8).found)
print(s.foundPairToSum(input,8).pair)

sol = Solution()
i = [1,2,3,9]
print(sol.fPTS(i,8))
i = [1,2,4,4]
print(sol.fPTS(i,8))
i = [-1,0,4,4,9]
print(sol.fPTS(i,8))

