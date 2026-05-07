class Solution:
    def balancedStringSplit(self, s: str) -> int:
        l,r=0,0
        sum=0
        for i in s:
            if i=='L':
                l+=1
            elif i=='R':
                r+=1
            
            if l==r:
                l,r=0,0
                sum+=1
        return sum