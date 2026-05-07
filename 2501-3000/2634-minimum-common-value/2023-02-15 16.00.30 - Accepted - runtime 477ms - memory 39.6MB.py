class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1=set(nums1)
        nums2=set(nums2)
        res=(nums1.intersection(nums2))
        res=list(res)
        if res!=[]:
            return min(res)

        return -1