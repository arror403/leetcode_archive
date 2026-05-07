class Solution:
    def minimumLength(self, s: str) -> int:
        res=len(s)
        t=[[k,len(list(g))] for k,g in groupby(s)]
        l,r=0,len(t)-1
        print(t)
        while l<r:
            if t[l][0]==t[r][0]:
                res-=(t[l][1]+t[r][1])
                l+=1
                r-=1
            else:
                break

        if l==r and t[l][1]>1: res-=t[l][1]

        return res