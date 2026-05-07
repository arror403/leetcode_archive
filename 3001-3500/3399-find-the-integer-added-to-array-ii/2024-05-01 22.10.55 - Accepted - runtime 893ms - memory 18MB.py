class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        res=inf
        d=Counter(nums1)
        nums1.sort()
        nums2.sort()
        
        m=list(combinations(d.keys(),2))+[(k,k) for k,f in d.items() if f>=2]

        for i,j in m:
            R=nums1[:]
            R.remove(i)
            R.remove(j)

            if len(set(b-a for a,b in zip(R,nums2)))==1:
                res=min(res, nums2[0]-R[0])

        return res