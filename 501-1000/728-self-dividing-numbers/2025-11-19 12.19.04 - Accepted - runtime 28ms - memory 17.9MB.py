class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res=[]

        for x in range(left, right+1):
            t=set(map(int,str(x)))
            if 0 in t: continue
            if all(x%v==0 for v in t):
                res.append(x)

        
        return res