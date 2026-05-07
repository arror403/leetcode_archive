class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        m=[i for i,v in enumerate(nums) if v==x]
        L=len(m)
        res=[]

        for x in queries:
            if x<=L:
                res.append(m[x-1])
            else:
                res+=[-1]

        return res