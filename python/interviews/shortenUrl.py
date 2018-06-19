import math
def intToShort(n):
  
  map = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
  s = ''
  
  while(n):
    print(n)
    print(n%62)
    print(map[32])
    s = s+map[n%62]
    n= (n/62)
    print(n)
    
  return (s)

def shortToInt(s):
  rId = 0;
  for each in reversed(s):
    if each >= 'a' and each <='z':
      rId = rId*62+ ord(each) - ord('a')
    elif each >= 'A' and each <='Z':
      rId = rId*62+ ord(each)- ord('A') +26
    elif each >= '0' and each <='9':
      rId = rId*62+ ord(each) - ord('0') +52
    else:
      continue
    print (rId)
  return rId
  
#print intToShort(899)
print (intToShort(900))
#print (ord('o')-ord('a'))
#print (ord('E')-ord('A'))
map = 'abcdefghijklmnopqrstuyvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
