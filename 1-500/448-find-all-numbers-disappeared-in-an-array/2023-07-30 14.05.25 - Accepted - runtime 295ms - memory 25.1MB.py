class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # Step 1: Mark elements in nums list
        for num in nums:
            idx = abs(num) - 1
            nums[idx] = -abs(nums[idx])
        
        # Step 2: Identify missing numbers
        res = []
        for i in range(n):
            if nums[i] > 0:
                res.append(i + 1)
        
        return res