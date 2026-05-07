class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        t=sorted(set(i+1 for i in range(n))-set(banned))
        
        return next((i for i,v in enumerate(accumulate(t)) if v>maxSum), len(t))