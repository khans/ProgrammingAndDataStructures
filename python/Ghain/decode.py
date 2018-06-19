# Example : "z3[a2[b]]rty3[ab]" = zabbabbabbrtyababab

class Solution():
    def decode(self,s):
        curNum = 0; cStr = ''; stack = []
        for c in s:
            print(stack,cStr,curNum)
            if c.isalpha():
                cStr += c
            elif c.isdigit():
                curNum = curNum*10 + int(c)
            elif c == '[':
                stack.append(cStr)
                stack.append(curNum)
                cStr = '' ; curNum = 0
            else:
                num = stack.pop()
                prev = stack.pop()
                cStr = prev + num * cStr
        return cStr
        

a = Solution()
print(a.decode("z3[a2[b]]rty3[ab]"))
                