class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        m=[[],[],[]]

        for v in nums:
            if v==pivot: 
                m[2]+=[v]
            else:
                m[v>pivot]+=[v]


        return m[0]+m[2]+m[1]