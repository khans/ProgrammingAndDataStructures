class Solution:
    def anaList(self,l):
        if len(l) <= 1:
            return l
        temp = {}
        for each in l:
            x = sorted(each)
            if x not in temp:
                temp[x] = [each]
            else:
                temp[x].append(each)
        return temp


s = Solution()
print(s.anaList(['batman','badcredit','appleinc','manbat','clanpipe','permasun','thehulk']))
            