class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 1
        min_in_partition = nums[0]
        
        for v in nums[1:]:
            if v - min_in_partition > k:
                res += 1
                min_in_partition = v
        

        return res