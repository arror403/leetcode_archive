class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        res = 0
        max_i_plus_val = 0  # values[i] + i

        for i, v in enumerate(values):
            # For each position j, we use the best values[i]+i we've seen so far and add it to (values[j]-j) to get values[i]+values[j]+i-j
            res = max(res, max_i_plus_val + v - i)
            max_i_plus_val = max(max_i_plus_val, v + i)

        
        return res