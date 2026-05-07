class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        if coins<min(costs): return 0
        costs.sort()
        res=0
        i=0
        # print(sum(costs))
        while i<len(costs) and coins >= costs[i]:
            coins-=costs[i]
            res+=1
            i+=1

        return res