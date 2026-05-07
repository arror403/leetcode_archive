class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res=0

        for i in range(low, high+1):
            L=len(str(i))
            if L%2!=0: continue

            t=list(map(int,str(i)))
            half=L//2

            res+=(sum(t[:half])==sum(t[half:]))


        return res