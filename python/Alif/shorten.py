def shorten(word,number):
  if number <=0:
    raise Exception('Passed in integer should not be less than or equal to Zero');
  n = len(word)
  check = n-number
  if check < 2:
    return word
  
  res = ''
  res = word[:number] + str(check-1) + word[-1]
  return res
  
print(shorten('Internationalization',1))
print(shorten('alpha',1))
print(shorten('alpha',2))
print(shorten('alpha',3))
print(shorten('alpha',4))
print(shorten('alpha',5))
print(shorten('alpha',6))
print(shorten('alpha',-1))
print(shorten('alpha',0))