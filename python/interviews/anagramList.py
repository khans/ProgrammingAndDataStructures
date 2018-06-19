#=====================================================================================================
def isAnagram(a1,a2):
  n = 0; m = 0;
  util = [0]*26
  for each in a1:
    if each >= 'a' and each <='z':
      util[ord(each)-ord('a')] += 1
      n += 1
    else:
      continue
  
  for each in a2:
    if each >= 'a' and each <='z':
      util[ord(each)-ord('a')] -= 1
      m += 1
    else:
      continue      
  
  for each in util:
    if each != 0:
      return False;
    else:
      pass
  return True
#=====================================================================================================
def isAnagram1(a1,a2):
  return sorted(a1) == sorted(a2)

#===================================================================================================== 

print(isAnagram('batman', 'SUPERMAN'))
print(isAnagram('apple inc', 'clan pipe   '))

#=====================================================================================================
anagrams = ['batman','superman','clan pipe','debit card','bad credit', 'apple inc', 'epic plan', 'man bat', 'perma sun', 'the hulk'];
#print (la(anagrams))
#=====================================================================================================
from collections import defaultdict
def la(l):
  res = []
  if len(l) <= 1:
    return res
    
  temp = []
  i = 0;
  while (i<len(l)):
    first = l[i]
    temp.append(first)
    j = i+1;
    while(j<len(l)):
      if (isAnagram(l[j],first)):
        temp.append(l[j])
        l.pop(j);
      else:
        j += 1;
    res.append(temp)
    temp = []
    i += 1
    
  
  print(res)


    
print(sorted(anagrams))  
la (anagrams)
print(sorted(anagrams))