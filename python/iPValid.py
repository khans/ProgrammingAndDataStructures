#IP validation

'''
7
1050:1000:1000:a000:5:600:300c:326b
1050:1000:2000:ab00:5:600:300c:326a
1050:1000:3000:abc0:5:600:300c:326c
1051:1000:4000:abcd:5:600:300c:326b
22.231.113.64
22.231.113.164
222.231.113.64
'''
import string
class Solution:
    def checkLine(self,line):
        if self.ipv4(line):
            return "IPv4"
        elif self.ipv6(line):
            return "IPv6"
        else:
            return "Neither"
    def ipv4(self,line):
        ch = False
        contents = line.split('.')
        if len(contents) == 4:
            for each in contents:
                x = int(each)
                if x >=0 and x<=255:
                    ch = True
                else:
                    ch = False
                    return ch
        return ch     
    def ipv6(self,line):
        ch = False
        contents = line.split(':')
        if len(contents) == 8:
            for each in contents:
                b = all (c in string.hexdigits for c in each)
                if(b):
                    ch = True
                else:
                    ch = False
                    return ch
        return ch
        

N= int(input())
if (N>0):
    for i in range (0,N):
        line = input()
        s = Solution()
        print(s.checkLine(line))
        
    