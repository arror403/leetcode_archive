class Solution:
    def minCosts(self, cost: List[int]) -> List[int]:
        return [cost[0]]+[min(cost[:i+1]) for i in range(1,len(cost))]