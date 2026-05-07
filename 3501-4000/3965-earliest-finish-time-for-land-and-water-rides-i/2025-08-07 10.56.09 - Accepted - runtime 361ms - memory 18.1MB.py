class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        res=inf

        for x,y in zip(landStartTime, landDuration):
            for p,q in zip(waterStartTime, waterDuration):
                res = min(res, p+q) if p>(x+y) else min(res, x+y+q)
                res = min(res, x+y) if x>(p+q) else min(res, p+q+y)
    

        return res