class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        return [k for k,f in Counter(arr).items() if f/len(arr)>0.25][0]