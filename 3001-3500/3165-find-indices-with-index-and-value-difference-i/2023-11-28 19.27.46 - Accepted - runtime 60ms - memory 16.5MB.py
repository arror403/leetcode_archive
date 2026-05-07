class Solution:
    def findIndices(self, nums: List[int], Di: int, Dv: int) -> List[int]:

        ##### power by chatGPT #####

        n = len(nums)
        for i in range(n):
            for j in range(i + Di, n):
                if abs(nums[i] - nums[j]) >= Dv:
                    return [i, j]
        return [-1, -1]