class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        t=list(chain.from_iterable(grid))
        return [next(k for k,v in Counter(t).items() if v==2), (set(range(1,len(t)+1))-set(t)).pop()]