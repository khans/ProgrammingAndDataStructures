#is Anagram
def isAnagram(s1,s2):
    if len(s1)!=len(s2):
        return False
    else:
        if len(s1) == 0:
            return True;
        if (len(s1) == 1):
            if(s1 == s2):
                return True
            else:
                return False
        else:
            charList = [0]*255;
            for each in s1:
                charList[ord(each)] = charList[ord(each)]+1
            for each in s2:
                charList[ord(each)] = charList[ord(each)]-1
        
            for each in charList:
                if each != 0:
                    return False
            return True


print isAnagram('pyar','ryap')


         
    
    