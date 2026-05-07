class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        localMax = nums[0]
        partitionIdx = 0
        M = localMax

        for i in range(1, len(nums)):
            if localMax > nums[i]:
                localMax = M
                partitionIdx = i
            else: 
                M = max(M, nums[i])


        return partitionIdx + 1