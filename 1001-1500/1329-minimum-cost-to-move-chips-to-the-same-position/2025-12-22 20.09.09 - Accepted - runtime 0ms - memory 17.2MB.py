class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        t=[0,0]
        for v in position: t[v%2]+=1

        return min(t[0],t[1])