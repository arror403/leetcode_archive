class Solution:
    def minCostToMoveChips(self, position: List[int]) -> int:
        odds = sum(x%2 for x in position)

        return min(odds, len(position)-odds)