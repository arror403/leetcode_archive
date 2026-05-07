class Solution:
    def longestContinuousSubstring(self, t: str) -> int:
        r,s=[],[]
        for i in t: r.append(ord(i)-97)
        
        for i in range(1,len(r)):
            tmp=r[i]-r[i-1]
            if tmp==1:
                s.append(1)
            else:
                s.append(0)
        
        m = [list(y) for x, y in groupby(s)]
        
        res=0
        
        for i in m:
            if i[0]==1:
                if len(i)>res:
                    res=len(i)
        print(r,s,m)
        return res+1