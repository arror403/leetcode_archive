class Solution:
    def firstUniqChar(self, s: str) -> int:
        s=list(s)
        d={}
        for i in s: d[i]=0
        for i in s: d[i]+=1
            
        for i in d: 
            # print(d[i],i)
            if d[i]==1:
                return s.index(str(i))
            
        return -1
        