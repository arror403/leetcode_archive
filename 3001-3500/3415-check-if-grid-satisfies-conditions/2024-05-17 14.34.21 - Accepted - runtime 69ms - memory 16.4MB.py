class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        return all(len(set(c))==1 for c in zip(*grid)) and all(r[i]!=r[i+1] for r in grid for i in range(len(r)-1))