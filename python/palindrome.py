#Return Yes or No if a string is a palindrome or not, ignore space, ignore punctuation, periods.

def isPalindrome(input):
    if (len(input)>0):
        tempList = []
        for each in input:
            if ((ord(each) in range(48,58)) or (ord(each) in range(65,123))):
                each = str.lower(each)
                tempList.append(each)
        if len(tempList) > 0:
            i = 0; 
            j = len(tempList)-1;

            while (i!=j and i<j):
                if tempList[i]!=tempList[j]:
                    return "No"
                i += 1; j -= 1
            return "Yes"
        else: 
            return "Invalid"
    return "Invalid"        


                
print (isPalindrome("Go hang a salami, I'm a lasagna hog"))
print (isPalindrome("A man, a plan, a canal, Panama."))
print (isPalindrome(''))
print (isPalindrome('90  09  22 22 9009 '))
print (isPalindrome(';+'))

class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        A = A.upper()
        i = 0; j = len(A)-1;
        if len(A)<=1:
            return 1
        while (i<=j):
           
            while(i<=j):
              if (ord(A[i]) not in range (97,123) and ord(A[i]) not in range (65,91) and ord(A[i]) not in range (48,58)):
                  i += 1
              else:
                break
            while(i<=j):      
              if (ord(A[j]) not in range (97,123) and ord(A[j]) not in range (65,91) and ord(A[j]) not in range (48,58)):
                  j -= 1
              else:
                break
            if i>j:
                i -=1
            if A[i]!=A[j]:
                return 0
            
            i +=1; j -= 1;
        return 1

s = Solution();
print (s.isPalindrome('""^'));
class Solution1:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        A = A.lower()
        n = len(A)
        low = 0
        high = n - 1
        ret = 1
        while low <= high:
            if A[low] == A[high]:
                low += 1
                high -= 1
                continue
            if str(A[low]).isalnum() and str(A[high]).isalnum():
                ret = 0
                break
            elif str(A[high]).isalnum():
                low += 1
            else:
                high -= 1
        return ret
