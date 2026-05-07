class Solution:
    def averageWaitingTime(self, r: List[List[int]]) -> float:
        res=r[0][1]
        cur=r[0][0]+r[0][1]
        L=len(r)
        r=r[1:]

        for a,b in r:
            if a<cur:
                res+=(b+cur-a)
                cur+=b
            else:
                res+=b
                cur=b+a
            

        return res/L