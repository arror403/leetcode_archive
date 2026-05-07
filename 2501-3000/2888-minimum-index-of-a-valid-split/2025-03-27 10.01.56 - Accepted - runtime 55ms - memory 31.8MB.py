class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # Boyer-Moore Majority Vote Algorithm to find candidate
        candidate = nums[0]
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        
        # Count occurrences of candidate
        total_count = nums.count(candidate)
        
        # If not truly majority, return -1
        if total_count * 2 <= len(nums):
            return -1
        
        # Track left side count
        left_count = 0
        for i in range(len(nums)):
            left_count += nums[i] == candidate
            right_count = total_count - left_count
            
            # Check split conditions
            if (left_count * 2 > i + 1) and (right_count * 2 > len(nums) - i - 1):
                return i
        
        return -1

# class Solution:
#     def minimumIndex(self, nums: List[int]) -> int:
#         n=len(nums)
#         x,f=Counter(nums).most_common(1)[0]
#         f1=1 if nums[0]==x else 0

#         for i in range(1,n):
#             if nums[i]==x: f1+=1
#             f2=f-f1
#             if ((f1/i)>0.5) and ((f2/(n-i))>0.5):
#                 return i-1


#         return -1