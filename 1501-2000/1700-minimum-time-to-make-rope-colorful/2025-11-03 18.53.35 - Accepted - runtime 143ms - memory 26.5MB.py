class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        res = 0
        max_cost = 0
        sum_cost = 0
        n = len(colors)

        for i in range(n):
            if i and colors[i] != colors[i-1]:
                res += (sum_cost - max_cost)
                sum_cost = 0
                max_cost = 0
            
            sum_cost += neededTime[i]
            max_cost = max(max_cost, neededTime[i])
        
        res += (sum_cost - max_cost)


        return res