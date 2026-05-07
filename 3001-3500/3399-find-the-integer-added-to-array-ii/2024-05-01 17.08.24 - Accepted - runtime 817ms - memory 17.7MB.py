class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        res=inf
        nums1.sort()
        nums2.sort()
        d=Counter(nums1)
        m=list(itertools.combinations(d.keys(),2))+[(k,k) for k,f in d.items() if f>=2]

        for i,j in m:
            R=nums1[:]
            R.remove(i)
            R.remove(j)

            if len(set([b-a for a,b in zip(R,nums2)]))==1:
                if nums2[0]-R[0]<res: 
                    res=nums2[0]-R[0]


        return res