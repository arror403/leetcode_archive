class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        if n <= 2: return min(cost)

        # Initialize two variables to store the minimum cost to reach the current and previous steps.
        prev_cost, curr_cost = cost[0], cost[1]

        for i in range(2, n):
            # Calculate the minimum cost to reach the current step.
            new_cost = cost[i] + min(prev_cost, curr_cost)
            
            # Update prev_cost and curr_cost for the next iteration.
            prev_cost, curr_cost = curr_cost, new_cost

        # The minimum cost to reach the top is either at the last or second-to-last step.
        return min(prev_cost, curr_cost)