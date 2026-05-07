class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        return next((k for k,g in groupby(arr) if len(list(g))>len(arr)/4))