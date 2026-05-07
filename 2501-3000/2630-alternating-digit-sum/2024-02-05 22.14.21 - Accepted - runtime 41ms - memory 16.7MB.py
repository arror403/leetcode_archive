class Solution:
    def alternateDigitSum(self, n: int) -> int:
        n=list(map(int,str(n)))
        res=0

        for i,v in enumerate(n):
            if i%2==0: res+=v
            else: res-=v

        return res