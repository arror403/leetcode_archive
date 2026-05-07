class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()

        d=Counter(nums1)
        res=inf
        
        m=list(itertools.combinations(d.keys(),2))
        for k,f in d.items():
            if f>=2: m.append((k,k))

        for i,j in m:
            R=nums1[:]

            R.remove(i)
            R.remove(j)

            if len(set([b-a for a,b in zip(R,nums2)]))==1:
                tmp=nums2[0]-R[0]
                if tmp<res:
                    res=tmp

        return res