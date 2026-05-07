class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        return False if len(arr)<3 else any((len(list(g))>=3 and k) for k,g in groupby(x%2 for x in arr))