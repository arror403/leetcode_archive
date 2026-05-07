class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        x=y=0

        for a in nums1: x^=a
        for b in nums2: y^=b


        return (len(nums1)%2*y)^(len(nums2)%2*x)



        # nums1=dict.fromkeys(nums1)
        # nums2=dict.fromkeys(nums2)
        # res=set()
        
        # for i in nums1:
        #     for j in nums2:
        #         res.add(i^j)


        # return list(res)