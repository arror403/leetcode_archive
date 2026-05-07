class Solution:
    def threeConsecutiveOdds(self, m: List[int]) -> bool:
        return 0 if len(m)<3 else any(len(list(g))>=3 and k==1 for k,g in groupby(map(lambda x:x%2,m)))