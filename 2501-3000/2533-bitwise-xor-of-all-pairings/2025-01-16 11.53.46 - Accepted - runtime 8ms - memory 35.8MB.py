class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        x=reduce(operator.xor, [0]+nums1)
        y=reduce(operator.xor, [0]+nums2)

        return (len(nums1)%2*y)^(len(nums2)%2*x)