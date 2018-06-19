# Is string2 a substring of string1

def isSubstring(main, small):
    if (len(main) == 0 and len(small)==0):
        return True
    elif (len(small) <= len(main)):
        if (len(small)!=0):
            tempList = []
            i = 0; j = 0;
            while(i<len(small) and j< len(main)):
                if small[i] == main[j]:
                    tempList.append(main[j])
                    i += 1; j += 1
                else:
                    tempList = []
                    j += 1
            
            tempList =  ''.join(tempList)
            #print(tempList)
            if (tempList == small):
                return True
            else:
                return False
        else:
            return True
    else:
        return False
        
print(isSubstring("preabates", "bat"))
print(isSubstring("curious",""))     
print(isSubstring("","p"))                
        
         