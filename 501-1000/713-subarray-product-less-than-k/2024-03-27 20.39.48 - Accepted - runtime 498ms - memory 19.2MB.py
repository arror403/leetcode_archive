class Solution:
    ##### taught by chatGPT #####
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        # If k is less than or equal to 1, no subarray can satisfy the condition
        if k==0 or k==1: return 0
        
        L=len(nums)
        res=0    # Initialize count of valid subarrays
        p=1      # Initialize product of elements within the window
        start=0  # Initialize left pointer
        
        for end in range(L):
            p*=nums[end]        # Expand the window by including the current element
            while p>=k:         # Shrink the window until the product is less than k
                p/=nums[start]  # Remove elements from the window
                start+=1        # Move the left pointer forward
            
            # Count subarrays ending at the current position (end)
            res+=(end-start+1)
            
        return res