#Given a compressed string of the form "3[ab2[c]]" return the decompressed string: "abccabccabcc"
# O(n)


def decompress(s):
    
    if (len(s) == 0):       
        return ""
    else:
        rStr = ''
        sStr = ''
        n = '' 
        inner = []
        for each in s:
            if (ord(each) in range (65,91) or ord(each) in range (97,123)): # is an alphabet
                rStr = rStr+each
            if ord(each) in range (48,58):      # get the count before the bracket
                n = n + each
            if (each=='['):
                inner = s[s.index(each)+1:-1]   #inner will be everything within the square brackets
                #inner.append(s[s.index(each)+1])
                i = 0
                
                while(i<int(n)):
                    sStr = sStr + (decompress(inner))
                    i += 1
                break
            
        return rStr+sStr
        


    

def tokenise(string):
    if len(string)<2:
        return string
    l = []
    brackets = [];
    number_of_brackets = 0;
    prevbracket =''
    currentbracket = ''
    n = 0
    m = 0
    answer = ''
    for each in string:
        l.append(each)
        if each == '[':
            currentbracket = each
            if prevbracket == '' or (currentbracket == prevbracket):
                n += 1
            brackets.append(currentbracket)
        if each == ']':
            currentbracket = each
            m += 1
            brackets.append(currentbracket)
        if n==m and n>0:
            answer = answer + decompress(''.join(l))
            l = []
            brackets = [];
            prevbracket =''
            currentbracket = ''
            n = 0
            m = 0
  
    answer = answer + decompress(''.join(l))
    return answer

'''
def splitStr(lStr):
    tempList = []
    tempList = lStr.split('.')
    answer = ''
    for each in tempList:
        answer = answer + decompress(each)
    return answer
'''            
            
    

#print(splitStr(tokenise('z3[a2[b]]2[a]')))   

print(decompress("z3[a2[b]]rty3[ab]"))
print(decompress("z1[a]"))
print(decompress("zab"))
print(decompress("2[2[zab]3[rtu]]"))
print(len(decompress('0[a2[b]]')))
print('z3[a2[b]].2[a].'.split('.'))
'''
print (tokenise('2z3[a2[b]]'))
print (tokenise(''))
print (tokenise('ab'))
print (tokenise('3[s]'))
print (tokenise("3[a]2[bc]"))         # return "aaabcbc".
print (tokenise("3[a2[c]]"))          # return "accaccacc".
print (tokenise("2[abc]3[cd]ef"))     # return "abcabccdcdcdef".
print (tokenise("2[abc4[ed4[u]]]3[cd]ef"))
print (tokenise("zxdsef"))
print (tokenise("zxd9[i2[jh]]sef"))
'''
#print (tokenise("zxd9000[i2[jh]]sef"))
