class Solution:
    def maximumHappinessSum(self, h: List[int], k: int) -> int:
        h.sort(reverse=True)
        res=h[0]
        t=1
        for x in h[1:k]:
            if (i:=x-t)>=0:
                res+=i
                t+=1
            else:
                break

        return res