class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        
        def solve(nums, previdx, chosenIndices):
            if len(chosenIndices) == len(nums): 
                return 1
            
            mask = 0
            for ind in chosenIndices: mask|=(1<<ind)
            
            if dp[previdx + 1][mask] != -1: 
                return dp[previdx + 1][mask]
        
            tot = 0
            for j in range(len(nums)):
                if j in chosenIndices:
                    continue
                if (previdx == -1 or nums[previdx] % nums[j] == 0 or nums[j] % nums[previdx] == 0):
                    chosenIndices.append(j)
                    tot += solve(nums, j, chosenIndices)
                    tot %= 10**9+7
                    chosenIndices.pop()

            dp[previdx + 1][mask] = tot

            return tot


        dp = [[-1] * ((1 << len(nums)) + 5) for _ in range(20)]
        chosenIndices = []


        return solve(nums, -1, chosenIndices)
