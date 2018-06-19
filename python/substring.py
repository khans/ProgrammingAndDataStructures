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
    
#print substring("cool",4,4)
#''
#print substring("cool",2,5)
#'ol