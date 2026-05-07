class Solution:
    def minimumBoxes(self, a: List[int], c: List[int]) -> int:
        return next(i+1 for i,v in enumerate(accumulate(sorted(c,reverse=1))) if v>=sum(a))