class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        res=0 
        max_e=max(candidates)
        b=1
        
        while b<=max_e:
            cnt=sum((n&b)>0 for n in candidates)
            res=max(res,cnt)
            b<<=1


        return res