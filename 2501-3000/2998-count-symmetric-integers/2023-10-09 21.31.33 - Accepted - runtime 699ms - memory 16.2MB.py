class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        res=0
        for i in range(low, high+1):
            if len(str(i))%2!=0: continue

            i=list(map(int,str(i)))
            half = len(i)//2
            if sum(i[:half])==sum(i[half:]): 
                # print(i)
                res+=1
        return res