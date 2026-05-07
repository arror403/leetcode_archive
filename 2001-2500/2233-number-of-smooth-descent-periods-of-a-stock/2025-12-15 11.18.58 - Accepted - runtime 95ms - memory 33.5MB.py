class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        m=[]
        i=res=0

        for j in range(len(prices)-1):
            if prices[j+1]==(prices[j]-1):
                continue
            else:
                m.append(prices[i:j+1])
                i=j+1

        m.append(prices[i:])
        # print(m)

        for g in m:
            n = len(g)
            res += n*(n+1)//2
        
        
        return res