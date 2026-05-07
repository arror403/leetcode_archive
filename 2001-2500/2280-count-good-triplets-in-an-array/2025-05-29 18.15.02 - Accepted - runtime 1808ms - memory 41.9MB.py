class Solution:
    def goodTriplets(self, nums1: List[int], nums2: List[int]) -> int:
        d={}
        st=[]
        res=0
        for i,v in enumerate(nums1): d[v]=i

        for x in nums2:
            idx=d[x]
            left=bisect_left(st, idx)
            right=(len(nums2)-1-idx)-(len(st)-left)
            res+=left*right
            insort(st, idx)


        return res