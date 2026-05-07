class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        r=[0,0]
        m=inf
        for v in nums1: 
            r[v%2]+=1
            if v%2: m=min(m,v)

        L=len(nums1)
        if r[0]==L or r[1]==L: return True

        for v in nums1:
            if v%2==0 and (v-m)<1: 
                return False


        return True