class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m=len(nums1)
        n=len(nums2)
        x=int((m+n)/2)
        b=(nums1+nums2)
        b.sort()
        if (m+n)%2==0:
            return((b[x-1]+b[x])/2)
        else:
            return b[x]