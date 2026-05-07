class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        L=len(nums2)
        d={v:i for i,v in enumerate(nums2)}
        res=[]

        for v in nums1:
            f=1
            for i in range(d[v]+1, L):
                if nums2[i]>v:
                    f=0
                    res.append(nums2[i])
                    break
            if f: res.append(-1)


        return res