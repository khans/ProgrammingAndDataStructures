"""Pig Latin is a language where we take the first letter of
a word and put it on the end while also adding a vowel sound. 
So dog becomes "ogday"
"""
pyg = 'ay'

original = raw_input('Enter a word:')

if len(original) > 0 and original.isalpha():
    #print original
    word = original.lower()
    first = word[0]
    if first == 'a' or first == 'e' or first == 'i' or first =='o' or first =='u':
        new_word = word+pyg
        print new_word
    else:
        new_word = word[1: len(word)] + first + pyg
        print new_word
else:
    print 'empty'
