class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res=[]
        j=0
        
        for i,v in enumerate(nums):
            if v==key:
                j=max(j, i-k)
                while j<=(i+k) and j<len(nums):
                    res.append(j)
                    j+=1


        return res