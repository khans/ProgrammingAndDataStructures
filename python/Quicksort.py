class Solution():
  def qsort(self,A,s,e):
    if(s<e):
      start = s       #indiices
      end = e
      pivotIndex = self.partition(A,start,end)
      self.qsort(A,start,pivotIndex-1)
      self.qsort(A,pivotIndex+1, end)
  
  def partition(self,A,start,end):
    pivot = A[end]
    pIndex = start
    for i in range(start,end-1):
      if (A[i] <= pivot):
        self.swap(A[i],A[pIndex])
        pIndex += 1
    self.swap(A[pIndex],A[end])
    return pIndex
  
  @classmethod  
  def swap(self,a,b):
    temp = a;
    a = b;
    b = temp;
    

#s = Solution()
B = [13,17,16,14,1,12,8,16,12]

  
def qsort(A,s,e):
    if(s<e):
      start = s       #indiices
      end = e
      pivotIndex = partition(A,start,end)
      print (pivotIndex)
      qsort(A,start,pivotIndex-1)
      qsort(A,pivotIndex+1, end)

def partition(A,start,end):
    pivot = A[end]
    pIndex = start
    for i in range(start,end):
      if (A[i] <= pivot):
        A[i],A[pIndex] = A[pIndex],A[i]
        pIndex += 1
    
    A[pIndex],A[end] = A[end],A[pIndex];

    return pIndex
 
def swap(a,b):
    temp = a;
    a = b;
    b = temp;
    #print (a,b)

qsort(B,0,len(B)-1)
print(B)
