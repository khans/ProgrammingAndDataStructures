
def compareVersion(v1,v2):
    l1 = v1.split('.')
    l2 = v2.split('.')
    len1 = len(l1)
    len2 = len(l2)
    if len1>len2:
        diff = len1-len2
        for i in range(diff):
            l2.append('0')
    elif len1 < len2:
        diff = len2-len1
        for i in range(diff):
            l1.append('0')
    else:
        pass
    print(l1)
    print(l2)
    for i in range(len(l1)):
        if (int(l1[i]) > int(l2[i])):
            return 1
        elif(int(l1[i]) < int(l2[i])):
            return -1
        else:
          continue
    return 0
    
print(compareVersion('1.1','1.2.3'))
    