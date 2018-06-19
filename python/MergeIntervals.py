# Definition for an interval.
class Interval:
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
        n = len(intervals)
        #print (n)
        x = new_interval.start
        y = new_interval.end
        if (x >y):
            x,y = y,x
        answer = []
        if n==0: 
            answer.append(new_interval)
            return answer
        else:
            tent = Interval()      #Initially tent is empty instance
            lastInterval = Interval()
            ch = False
            for i in range(0,n):
                #print (tent)
                x1= intervals[i].start
                y1 = intervals[i].end
                if (ch): 
                    x = x1
                    y = y1
                    x1= tent.start
                    y1 = tent.end
                if (x >= x1 and x <= y1):
                    #print ("w")
                    tent.start = x1
                    tent.end = max(y1,y)
                    lastInterval = tent
                    ch = True
                if (x < x1):
                    #print ("x")
                    if(y<x1):
                        answer.append(Interval(x,y))
                        tent.start = x1; tent.end = y1; 
                        
                    else:
                        tent.start = x
                        tent.end = max(y1,y)
                    lastInterval = tent
                    ch = True
                if (x>y1):
                   # print ("y")
                    
                    answer.append(Interval(x1,y1))
                    if (ch):
                      tent.start = x
                      tent.end = y
                    lastInterval.start = x
                    lastInterval.end = y
            answer.append(lastInterval)
        return answer

A = [Interval(3,6),Interval(8,10)]
B = Interval(1,2)
s = Solution()
print(s.insert(A,B))
for each in s.insert(A,B):
  print(each.start,each.end)