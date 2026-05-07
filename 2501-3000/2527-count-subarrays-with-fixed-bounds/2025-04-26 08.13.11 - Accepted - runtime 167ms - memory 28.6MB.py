class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        res=0
        prevMinKIndex=prevMaxKIndex=j=-1

        for i,v in enumerate(nums):
            if v<minK or v>maxK:
                j=i
            if v==minK:
                prevMinKIndex=i
            if v==maxK:
                prevMaxKIndex=i

            res+=max(0, min(prevMinKIndex, prevMaxKIndex)-j)


        return res