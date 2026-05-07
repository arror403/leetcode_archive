class Solution:
    def findChampion(self, grid: List[List[int]]) -> int:
        L=len(grid)-1
        for i,r in enumerate(grid):
            if sum(r)==L:
                return i