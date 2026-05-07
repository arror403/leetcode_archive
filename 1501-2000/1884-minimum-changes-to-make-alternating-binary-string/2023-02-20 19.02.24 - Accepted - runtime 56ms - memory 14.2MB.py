class Solution:
    def minOperations(self, s: str) -> int:
        m,n=0,0
        x,y='',''
        for i in range(int(len(s)/2)): x+='01'
        if len(s)%2==1: x+='0'
        for i in range(int(len(s)/2)): y+='10'
        if len(s)%2==1: y+='1'

        # print(x)
        # print(y)
        for i in range(len(s)):
            if s[i]!=x[i]: m+=1
            if s[i]!=y[i]: n+=1

        return min(m,n)