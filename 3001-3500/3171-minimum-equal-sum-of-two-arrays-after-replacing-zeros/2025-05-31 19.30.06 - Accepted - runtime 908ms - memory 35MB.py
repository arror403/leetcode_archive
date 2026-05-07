class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum1, zeros1 = sum(nums1), nums1.count(0)
        sum2, zeros2 = sum(nums2), nums2.count(0)
        min1 = sum1 + zeros1
        min2 = sum2 + zeros2
        
        if zeros1 == 0 and sum1 < min2: return -1
        if zeros2 == 0 and sum2 < min1: return -1
        
        return max(min1, min2)