class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        if a>b: tmp=b
        else: tmp=a
        res=0

        for i in range(1,tmp+1):
            if a%i==0 and b%i==0: res+=1

        return res