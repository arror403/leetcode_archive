class Solution:
    ##### power by chatGPT #####
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n
        
        # Calculate prefix products and update result
        prefix_product = 1
        for i in range(n):
            result[i] *= prefix_product
            prefix_product *= nums[i]
        
        # Calculate suffix products using suffix_product variable
        suffix_product = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix_product
            suffix_product *= nums[i]
        
        return result