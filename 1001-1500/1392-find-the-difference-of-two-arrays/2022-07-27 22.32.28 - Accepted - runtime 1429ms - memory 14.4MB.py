class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        m,n,res=[],[],[]
        
        for i in nums1:
            if i not in nums2:
                m.append(i)
                
        for i in nums2:
            if i not in nums1:
                n.append(i)
        m=list(set(m))
        n=list(set(n))
        res.append(m)
        res.append(n)
        
        return res
