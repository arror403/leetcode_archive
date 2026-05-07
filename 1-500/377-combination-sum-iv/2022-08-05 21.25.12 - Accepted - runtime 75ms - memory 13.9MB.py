class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        comb=[0]*(target + 1)
        comb[0] = 1
        for i in range(len(comb)):
            for j in range(len(nums)):
                if (i - nums[j] >= 0):
                    comb[i] += comb[i - nums[j]]
        return comb[target]

