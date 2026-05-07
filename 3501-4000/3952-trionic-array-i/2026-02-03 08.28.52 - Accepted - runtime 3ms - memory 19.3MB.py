class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        L=len(nums)
        p=q=-1

        for j in range(1, L-1):
            if nums[j-1] >= nums[j]:  # Changed: check if NOT strictly increasing
                break
            if nums[j] >= nums[j+1]:  # Found end of increasing part
                p = j
                break

        if p==-1: return False

        for j in range(p+1, L-1):
            if nums[j-1] <= nums[j]:  # Changed: check if NOT strictly decreasing
                break
            if nums[j] <= nums[j+1]:  # Found end of decreasing part
                q = j
                break
 
        if q==-1: return False
            
        # Check if remaining part is strictly increasing
        for j in range(q, L-1):
            if nums[j] >= nums[j+1]:
                return False


        return True