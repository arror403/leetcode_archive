class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr)<3: return 0
        return any(len(list(g))>=3 and k==1 for k,g in groupby(map(lambda x: x%2, arr)))