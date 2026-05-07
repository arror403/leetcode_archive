class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        if any(num < k for num in nums): return -1

        if all(num == k for num in nums): return 0
        
        unique_values = sorted(set(nums), reverse=True)
        operations = 0
        
        i = 0
        while i < len(unique_values) and unique_values[i] > k:
            current = unique_values[i]
            
            # Find the next valid h (all values > h must be equal)
            # At each step, we can only go to the next value in our sorted list
            # because that ensures all values > h are identical (they're all = current)
            i += 1
            operations += 1
        

        return operations



# class Solution:
#     def minOperations(self, nums: List[int], k: int) -> int:
#         if len(set(nums))==1:
#             if nums[0]==k:
#                 return 0

#         t=sum(v>k for v in set(nums))


#         return t if t else -1