#Pascal's Triangle:
'''
[
     [1],
     [1,1],
     [1,2,1],
     [1,3,3,1],
     [1,4,6,4,1]
]
'''
class Solution:
    # @param A : integer
    # @return a list of list of integers
    def generate(self, A):
        answer = []
        if A == 0:
            return answer
        row0 = [1]
        if A == 1:
            answer = [[1]]
            return answer
        else:
            row1=[1,1]
            answer = [row0,row1]
            prev = row1
            for i in range(A-2):
                curr = self.currList(prev)
                answer.append(curr)
                prev = curr
        return answer
    def currList(self,pl):
        curr = [1,1]
        for i in range(1,len(pl)):
            v = pl[i]+pl[i-1]
            curr.insert(i,v)
        return curr
