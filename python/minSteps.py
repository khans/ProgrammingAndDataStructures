class Solution():
    # @param X : list of integers
    # @param Y : list of integers
    # Points are represented by (X[i], Y[i])
    # @return an integer
    @classmethod
    def coverPoints(self, X, Y):
      if (len(X) != len(Y)):
        return "Invalid Input, the size needs to be the same for both arrays"
      steps = 0
      n = len(X)
      if n == 0: return steps
      for i in range (n-1):
        steps = steps + max(abs(X[i+1]-X[i]), abs(Y[i+1]-Y[i]))
      return steps

thing = Solution()
print(thing.coverPoints([1,5,11],[0,9,13]))
print(thing.coverPoints([0,0,0],[0,0,0]))
print(thing.coverPoints([],[]))
print(thing.coverPoints([0,0,0],[0,0,0]))
print(thing.coverPoints([0,0,0],[0,0,0,5]))
A = [ 4, 8, -7, -5, -13, 9, -7, 8 ]
B = [ 4, -15, -10, -3, -13, 12, 8, -8 ]

print(thing.coverPoints(A,B))        