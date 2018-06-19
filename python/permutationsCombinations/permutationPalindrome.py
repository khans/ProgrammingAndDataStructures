import unittest
#Write an efficient function that checks whether any permutation of an input string is a palindrome. 
#O(n) is time complexity, O(1) or O(k) is space complexity
'''Examples:

"civic" should return True
"ivicc" should return True
"civil" should return False
"livci" should return False
'''
def cP(s):
  h = {}
  for each in s:
    if each not in h:
      h[each] = 1
    else:
      h[each]+=1
  odds = 0
  for k,v in h.items():
    if v%2 ==1:
      odds += 1
    if odds > 1:
      return 0
  return 1

def cP1(s):
    t = set()
    for each in s:
      if each not in t:
        t.add(each)
      else:
        t.remove(each)
    return len(t)<=1
assert( cP1("civic") == True ) 
assert( cP1("ivicc") == True ) 
assert( cP1("civil") == False ) 
assert( cP1("livci") == False )

'''
  def has_palindrome_permutation(the_string):

    # track characters we've seen an odd number of times
    unpaired_characters = set()

    for char in the_string:
        if char in unpaired_characters:
            unpaired_characters.remove(char)
        else:
            unpaired_characters.add(char)

    # the string has a palindrome permutation if it
    # has one or zero characters without a pair
    return len(unpaired_characters) <= 1
'''