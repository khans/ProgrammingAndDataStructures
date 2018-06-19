def substring(string,offset,end):
    
    if string == "":
        return ""
    if offset > end:
        return ""
    if offset > len(string)-1:
        return ""
    if end > len(string)-1:
        return substring(string,offset,len(string)-1)
    s = ""
    i = offset
    for i in range(offset, end+1):
        s = s+string[i]
    return s

def subexists(string,sub):
    if len(sub)>len(string):
        return False
    if sub == '':
        return True
    if string == sub:
        return True
    flag = 1
    for i in range(0,len(string)):
        for j in range(0,len(sub)):
            if string[i] != sub[j]:
                flag = 0
                break
            if string[i] == sub[j]:
                if substring(string,i,i+len(sub)-1) == sub:
                    flag = 1
                    
                    return True
                else:
                    flag = 0
                    break
        continue
    if flag == 0:
        return False

'''
subexists("Hello "," ")
True
subexists("Hello ","k ")
False
subexists("Hello ","Hell")
True
'''
   
    
